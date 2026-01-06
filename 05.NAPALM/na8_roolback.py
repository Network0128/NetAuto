import time
from napalm import get_network_driver

driver = get_network_driver('ios')

# 1. global_delay_factor: 명령어 입력 후 대기 시간 (느린 장비 배려)
# 2. conn_timeout: SSH 접속 시도 대기 시간 (기본 5초 -> 20초로 증가)
switch1 = driver(
    '10.1.1.11', 
    'ccnp', 
    'cisco', 
    optional_args={
        'global_delay_factor': 10,
        'conn_timeout': 20
    }
)

print('--- 장비에 연결 중입니다... ---')
# 여기서 에러가 난다면 100% 장비 VTY 라인이 꽉 찬 것입니다.
switch1.open()

try:
    print('\n[Step 1] bad_config.cfg 로드 중...')
    switch1.load_merge_candidate(filename='bad_config.cfg')
    
    diffs = switch1.compare_config()

    if len(diffs) > 0:
        print(diffs)
        
        print('>>> Commit (적용)...')
        switch1.commit_config()
        print('>>> 적용 완료. 5초 대기...')
        time.sleep(5)

        print('>>> Rollback (복구)...')
        switch1.rollback()
        print('>>> 복구 완료.')
        
    else:
        print('변경 사항 없음.')
        switch1.discard_config()

except Exception as e:
    print(f'Error: {e}')

finally:
    switch1.close()
    print('연결 종료.')
