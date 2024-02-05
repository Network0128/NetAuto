#Netmiko를 사용하여 여러 Cisco 장비에 대해 "show ip int brief" 명령을 실행합니다.

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": password,
}

switch1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.11",
    "username": "ccnp",
    "password": password,
}

switch2 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.12",
    "username": "ccnp",
    "password": password,
}

switch3 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.13",
    "username": "ccnp",
    "password": password,
}

command="show ip int brief"

for device in (router1, switch1, switch2, switch3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt) #생략가능
        output = net_connect.send_command(command)
        print(output)
