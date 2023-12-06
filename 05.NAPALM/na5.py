from napalm import get_network_driver
driver = get_network_driver('ios') # 'ios' : Cisco IOS 장비 사용
switch1 = driver('10.1.1.11', 'ccnp', 'cisco') # IP 주소와 인증 정보로 연결 객체 생성
# 필요시 위에 추가 : optional_args={'dest_file_system': 'flash0:'}

switch1.open() # 장비 연결

print('Accessing 10.1.1.11')

switch1.load_merge_candidate(filename='Merge1.cfg') #새로운 설정 로드(병합)

print(switch1.compare_config()) # 변경 사항 확인
switch1.commit_config() # 변경 사항 커밋(적용)

switch1.close() # 연결 종료
