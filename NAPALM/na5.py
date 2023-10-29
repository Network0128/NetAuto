from napalm import get_network_driver
driver = get_network_driver('ios')
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')
switch1.open()

print('Accessing 10.1.1.11')

switch1.load_merge_candidate(filename='ACL1.cfg') #새로운 설정 로드

print(switch1.compare_config()) # 변경 사항 확인
switch1.commit_config() # 변경 사항 커밋(적용)

switch1.close()
