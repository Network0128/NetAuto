#napalm 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 
#해당 장치로부터 정보를 가져와 출력하는 과정을 수행

import napalm  # napalm 라이브러리 가져오기

# 드라이버 설정 : 접속하는 장비의 유형('ios', 'nxos', 'junos' 등)
driver = napalm.get_network_driver('ios')  # 'ios' 드라이버 가져오기
# 장비에 연결
device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')  # 장치 연결 정보 설정
device.open()  # 장치에 연결 시작

#get_facts() 메서드 : 장비 정보 가져오기(장비 모델, 시리얼 번호, 운영 체제 버전 등)
output = device.get_facts()  # 장치로부터 사실 가져오기

print(output)  # 화면에 출력

device.close()  # 장치 연결 닫기
