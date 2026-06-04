#Netmiko를 사용하여 여러 Cisco 장비에 대해 "show ip int brief" 명령을 실행합니다.

from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
}

router2 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
}

switch1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.11",
    "username": "ccnp",
    "password": "cisco",
}

switch2 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.12",
    "username": "ccnp",
    "password": "cisco",
}

switch3 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.13",
    "username": "ccnp",
    "password": "cisco",
}

command="show ip int brief"

for device in (router1, router2, switch1, switch2, switch3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        print(net_connect.send_command(command))
        print()
---------------------------------------------------------------------------
ㅁ 여러 장비에 차례대로 리스트로 되어 있는 여러 명령어를 실행할 경우 ㅁ
commands=["show ip int brief","show ip arp"]

for device in (router1, router2, switch1, switch2, switch3):
    with ConnectHandler(**device) as net_connect:
        for cmd in commands:
            print(net_connect.find_prompt())
            print(net_connect.send_command(cmd))
            print()
---------------------------------------------------------------------------
ㅁ 모든 장비의 설정 파일 저장 ㅁ
for device in (router1,router2,switch1,switch2,switch3):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command("show run")
        file_name = f"device_{device['host']}.txt"
        with open(file_name,'w') as save_file:
            save_file.write(output)
        print(f"백업 성공: {file_name}")
---------------------------------------------------------------------------

ㅁ 모든 장비의 설정 파일 저장 - 모든 장비의 목록 파일을 활용하기 ㅁ
from netmiko import ConnectHandler

# 공통 인증 정보 정의
user, password = "ccnp", "cisco"

# 1. IP 목록이 저장된 all_devices 파일을 읽기 모드로 오픈 (자동 Close)
with open('all_devices', 'r', encoding='utf-8') as f:
    for IP in f:
        IP = IP.strip() # 줄바꿈(\n) 및 양끝 공백 제거
        
        # 빈 줄이 있을 경우 에러 방지를 위해 패스
        if not IP:
            continue
            
        print(f'Get running Config from Device {IP} via SSH')
        
        # 각 IP를 순회할 때마다 host 항목에 동적으로 대입하여 딕셔너리 생성
        device_info = {
            "device_type": "cisco_ios",
            "host": IP,
            "username": user,
            "password": password,
        }
        
        # 2. Netmiko SSH 연결 시작 (자동 Close)
        with ConnectHandler(**device_info) as net_connect:
            # show running-config 명령어를 수행하여 결과를 변수에 저장
            output = net_connect.send_command("show running-config")
            
            # 3. 장비별 결과 파일 오픈 및 기록 (자동 Close)
            with open(f'device_{IP}.txt', 'w', encoding='utf-8') as save:
                save.write(output)
