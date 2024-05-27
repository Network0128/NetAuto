#Netmiko를 사용하여 여러 Cisco 장비에 대해 "show ip int brief" 명령을 실행합니다.

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

command="show ip int brief"

for device in (router1, switch1, switch2, switch3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.send_command(command))
