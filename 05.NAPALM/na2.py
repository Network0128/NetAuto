#NAPALM 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 해당 장치의 모든 인터페이스 정보를 가져와 출력하는 과정을 수행

from napalm import get_network_driver  # napalm 라이브러리에서 get_network_driver 함수 가져오기

driver = get_network_driver('ios')  # 'ios' 드라이버 가져오기

device = driver(hostname='10.1.1.3', username='ccnp', password='cisco')  # 장치 연결 정보 설정

device.open()  # 장치에 연결 시작

interfaces = device.get_interfaces()  # 모든 인터페이스 정보 가져오기

print(interfaces)  # 인터페이스 정보 출력

device.close()  # 장치 연결 종료

