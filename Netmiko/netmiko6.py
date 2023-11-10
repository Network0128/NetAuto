from netmiko import ConnectHandler
from getpass import getpass

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.3",
    "username": "ccnp",
    "password": getpass(),
}

commands = ["logging buffered 100000"]
with ConnectHandler(**router1) as net_connect:
    output = net_connect.send_config_set(commands) #send_config_set: 전역 설정 모드의 명령어를 보내는데 사용
    output += net_connect.save_config() #네트워크 장비의 현재 설정 저장

print()
print(output)
print()