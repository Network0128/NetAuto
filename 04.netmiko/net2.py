# Netmiko 라이브러리를 사용하여 3개의 Cisco 스위치에 연결하고 VLAN 2부터 10까지 생성

from netmiko import ConnectHandler  # Netmiko 라이브러리를 임포트하여 네트워크 장비 자동화

# 첫 번째 스위치 연결 정보
switch1 = {
    'device_type': 'cisco_ios',  # 디바이스 타입으로 cisco_ios 지정
    'ip': '10.1.1.11',  # 스위치의 IP 주소
    'username': 'ccnp',  # 접속을 위한 사용자 이름
    'password': 'cisco'  # 접속을 위한 비밀번호
}

# 두 번째 스위치 연결 정보
switch2 = {
    'device_type': 'cisco_ios',  # 디바이스 타입으로 cisco_ios 지정
    'ip': '10.1.1.12',  # 스위치의 IP 주소
    'username': 'ccnp',  # 접속을 위한 사용자 이름
    'password': 'cisco'  # 접속을 위한 비밀번호
}

# 세 번째 스위치 연결 정보
switch3 = {
    'device_type': 'cisco_ios',  # 디바이스 타입으로 cisco_ios 지정
    'ip': '10.1.1.13',  # 스위치의 IP 주소
    'username': 'ccnp',  # 접속을 위한 사용자 이름
    'password': 'cisco'  # 접속을 위한 비밀번호
}

devices = [switch1, switch2, switch3]  # 연결할 스위치 목록

for device in devices:  # 각 스위치에 대해 반복
    net_connect = ConnectHandler(**device)  # 스위치에 연결
    for n in range(2, 11):  # VLAN 2부터 10까지 생성
        print("Creating VLAN " + str(n))  # 생성 중인 VLAN 번호 출력
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]  # VLAN 생성 및 이름 지정 명령어
        output = net_connect.send_config_set(config_commands)  # 명령어 실행 및 출력
        print(output)  # 실행 결과 출력
