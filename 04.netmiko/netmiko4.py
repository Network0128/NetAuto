from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.3",
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
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    print(output)
    net_connect.disconnect()