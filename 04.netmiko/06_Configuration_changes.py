# Cisco IOS 장비의 설정을 변경하고 저장하는 과정을 자동화합니다.
# send_config_set과 save_config 메소드를 통해 설정 파일을 변경하고, 저장합니다.

from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
}

#commands = ["logging buffered 100000"] #라우터의 내부 로깅 버퍼 크기를 100,000바이트로 설정
commands = ["interface loopback 0", "ip address 1.1.1.1 255.255.255.0"]

with ConnectHandler(**router1) as net_connect:
    output = net_connect.send_config_set(commands) #send_config_set: 전역 설정 모드의 명령어를 보내는데 사용
    output += net_connect.save_config() #네트워크 장비의 현재 설정 저장
    # ---------위의 2줄 아래와 같이 가능-------------#
    # print(net_connect.send_config_set(commands)) #
    # print(net_connect.save_config())             #

print()
print(output)
print()
--------------------------------------------------------------
#여러 장비에 동시에 설정 및 저장
from netmiko import ConnectHandler

router1 = {
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

#command="show ip int brief"
commands = ["interface loopback 0", "ip address 1.1.1.1 255.255.255.0"]

for device in (router1, switch1, switch2, switch3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        output=net_connect.send_config_set(commands)
        output += net_connect.save_config()
        #output += net_connect.send_command(command)        
        print(output)
        print()
