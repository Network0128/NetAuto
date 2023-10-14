from netmiko import ConnectHandler
from getpass import getpass

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.3",
    "username": "ccnp",
    "password": getpass(),
}

net_connect = ConnectHandler(**router1) # **router1 : 딕셔너리의 각 키-값 쌍이 함수의 인자로 전달
output = net_connect.send_command("show ip int brief")
print(output)
output = net_connect.send_command("show run")
print(output)
net_connect.disconnect()