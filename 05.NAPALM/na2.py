# NAPALM 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 
# 해당 장치의 모든 인터페이스 정보 출력

from napalm import get_network_driver  # napalm 라이브러리에서 get_network_driver 함수 가져오기
driver = get_network_driver('ios')  # 'ios' 드라이버 가져오기
device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')  # 장치 연결 정보 설정
device.open()  # 장치에 연결 시작
interfaces = device.get_interfaces()  # 모든 인터페이스 정보 가져오기
print(interfaces)  # 인터페이스 정보 출력
device.close()  # 장치 연결 종료

---------------------------------------------------

# 인터페이스 정보 출력부분만 아래와 같이 수정

for interface_name in interface:
    print(interface_name, interface[interface_name])  # 각 인터페이스의 이름과 상세 정보 출력

# interface : 모든 인터페이스 정보를 담은 사전(dictionary)
# interface_name: 각 인터페이스의 이름(예: GigabitEthernet0/0)

---------------------------------------------------

