# switch_design 파일의 설정 명령어를 읽어 들입니다.
# 3개의 Cisco IOS 스위치에 차례로 연결하여 읽어 들인 설정 명령어를 실행합니다.

from netmiko import ConnectHandler

switch1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.11',
    'username': 'ccnp',
    'password': 'cisco'
}

switch2 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.12',
    'username': 'ccnp',
    'password': 'cisco'
}

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.13',
    'username': 'ccnp',
    'password': 'cisco'
}

with open('switch_design') as f: # switch_design 파일 읽기
    lines = f.read().splitlines() # 파일 내용을 줄 단위로 리스트로 저장
print(lines) # 파일 내용 출력

devices = [switch1, switch2, switch3] # 스위치 목록 정의

for device in devices: # 각 스위치에 연결하여 명령어 실행
    net_connect = ConnectHandler(**device) # 스위치에 연결
    output = net_connect.send_config_set(lines) # 설정 명령어 실행
    print(output)  # 실행 결과 출력
