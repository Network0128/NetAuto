import time
from napalm import get_network_driver

driver = get_network_driver('ios')

# [핵심] conn_timeout을 60초까지 늘려서 무조건 접속되게 설정
switch1 = driver(
    '10.1.1.11', 
    'ccnp', 
    'cisco', 
    optional_args={
        'global_delay_factor': 20,     # 명령어 반응 대기 (느림보 장비용)
        'conn_timeout': 60,            # SSH 접속 대기 (문 열어줄 때까지 1분 기다림)
        'dest_file_system': 'flash0:', # 파일 저장 위치 고정
    }
)

print('--- 1. 장비 접속 시도 (최대 60초 대기) ---')
# 여기서 에러가 나면 100% 장비 문제입니다 (재부팅 필수)
switch1.open()
print('--- 접속 성공! ---')

try:
    print('--- 2. 설정 파일 로드 ---')
    switch1.load_merge_candidate(filename='bad_config.cfg')
    
    print('--- 3. 변경 사항 비교 ---')
    diffs = switch1.compare_config()

    if len(diffs) > 0:
        print(diffs)
        print('>>> Commit (적용)...')
        switch1.commit_config()
        
        print('>>> 5초 대기...')
        time.sleep(5)

        print('>>> Rollback (복구)...')
        switch1.rollback()
        print('>>> 복구 완료.')
    else:
        print('변경 사항 없음.')
        switch1.discard_config()

except Exception as e:
    print(f"\n[에러 발생] {e}")

finally:
    switch1.close()
    print('연결 종료.')
