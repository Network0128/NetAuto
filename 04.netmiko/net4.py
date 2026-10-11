# switch_config 파일의 설정 명령어를 읽어 3개의 스위치에 차례로 연결 및 실행
# router_config 파일의 설정 명령어를 읽어 라우터에 연결 및 실행

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

router1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.21',
    'username': 'ccnp',
    'password': 'cisco'
}

router2 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.22',
    'username': 'ccnp',
    'password': 'cisco'
}

with open('switch_config') as f:
    lines = f.read().splitlines()

devices = [switch1, switch2, switch3]
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)

#router_design 파일 열어서 실행
with open('router_config') as f: # router_config 파일 읽기
    lines = f.read().splitlines() # 파일 내용을 줄 단위로 리스트로 저장

# 라우터에 설정 명령어 실행
devices = [router1, router2] # 라우터 목록, 여러개 라우터가 추가될 경우 대비
for device in devices:
    net_connect = ConnectHandler(**device) # 라우터에 연결
    output = net_connect.send_config_set(lines) # 설정 명령어 실행
    print(output) # 실행 결과 출력


