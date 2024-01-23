from netmiko import ConnectHandler
from getpass import getpass

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": getpass(),
}

# Will automatically 'disconnect()'
with ConnectHandler(**router1) as net_connect:
    print(net_connect.find_prompt())
    output = net_connect.send_command("show ip int brief")
    print(output)
