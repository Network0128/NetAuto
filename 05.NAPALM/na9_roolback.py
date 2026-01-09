import time
from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(
    '10.1.1.11', 
    'ccnp', 
    'cisco', 
    optional_args={
        'global_delay_factor': 20,     # 명령어 반응 대기 (느림보 장비용)
        'dest_file_system': 'flash0:', # 파일 저장 위치 고정
        'timeout': 120                 # 명령어가 완료될 때까지 최대 2분 기다림
    }
)

print('--- 1. 장비 접속 시도 (최대 60초 대기) ---')
# 여기서 에러가 나면 100% 장비 문제입니다 (재부팅 필수)
device.open()
print('--- 접속 성공! ---')

try:
    print('--- 2. 설정 파일 로드 ---')
    device.load_merge_candidate(filename='bad_config.cfg')
    
    print('--- 3. 변경 사항 비교 ---')
    diffs = device.compare_config()

    if len(diffs) > 0:
        print(diffs)
        print('>>> Commit (적용)...')
        device.commit_config()
        
        print('>>> 5초 대기...')
        time.sleep(5)

        print('>>> Rollback (복구)...')
        device.rollback()
        print('>>> 복구 완료.')
    else:
        print('변경 사항 없음.')
        device.discard_config()

except Exception as e:
    print(f"\n[에러 발생] {e}")

finally:
    device.close()
    print('연결 종료.')
