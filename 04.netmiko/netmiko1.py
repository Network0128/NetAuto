from netmiko import ConnectHandler 
from getpass import getpass 

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="R1",
    username="ccnp",
    password=getpass()
)

output = net_connect.send_command("show ip int brief") 
print(output)
output = net_connect.send_command("show run") 
print(output)

net_connect.disconnect()