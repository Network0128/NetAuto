#Cisco NXOS 스위치에 연결하고 IP 인터페이스 정보를 출력합니다.
#루프백 인터페이스를 생성하고 IP 주소를 설정하며, VLAN 2부터 10까지 생성합니다.

# Netmiko 라이브러리 임포트
from netmiko import ConnectHandler

# NXOS 스위치 연결 정보 정의
NXOS1 = {
 'device_type': 'cisco_nxos',  # 디바이스 타입: cisco_nxos 지
 'ip': '10.1.1.20',  # 스위치의 IP 주소
 'username': 'ccnp',  # 접속을 위한 사용자 이름
 'password': 'cisco123!'  # 접속을 위한 비밀번호
}

# NXOS 스위치에 연결
net_connect = ConnectHandler(**NXOS1)

# IP 인터페이스 정보 출력
output = net_connect.send_command('show ip interface brief')
print(output)

# 루프백 인터페이스 생성 및 IP 주소 설정
config_commands = ['interface loopback0', 'ip address 1.1.1.1/24']
output = net_connect.send_config_set(config_commands) # 설정 명령어를 스위치에 전송
print(output) # 설정 명령어의 출력 결과 출력


# VLAN 2부터 10까지 생성
for n in range(2, 11):
 print("Creating VLAN " + str(n)) # VLAN 생성 중임을 나타내는 메시지 출력
 config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)] # VLAN 생성 및 이름 지정 명령어
 output = net_connect.send_config_set(config_commands) # VLAN 구성 명령어를 스위치에 전송
 print(output) # VLAN 구성 명령어의 출력 결과 출력
