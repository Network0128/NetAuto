#napalm 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 
#해당 장치로부터 정보를 가져와 출력하는 과정을 수행

import napalm  # napalm 라이브러리 가져오기

driver = napalm.get_network_driver('ios')  # 'ios' 드라이버 가져오기

device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')  # 장치 연결 정보 설정

device.open()  # 장치에 연결 시작

output = device.get_facts()  # 장치로부터 사실 가져오기

print(output)  # 출력 인쇄

device.close()  # 장치 연결 닫기
