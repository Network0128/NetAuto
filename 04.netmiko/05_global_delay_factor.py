from netmiko import ConnectHandler
from getpass import getpass

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": getpass(),
    "global_delay_factor": 2, #﻿모든 지연 시간을 2배로 증가시킨다.
}

command = "show ip arp"
net_connect = ConnectHandler(**router1)
output = net_connect.send_command(command)
net_connect.disconnect()

print(f"\n{output}\n")
