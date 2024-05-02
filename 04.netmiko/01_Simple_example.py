from netmiko import ConnectHandler 
from getpass import getpass 

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="10.1.1.21",
    username="ccnp",
    password=getpass()
)

output = net_connect.send_command("show ip int brief") #send_command: 관리자 모드의 명령어를 보내는데 사용
print(output)
output = net_connect.send_command("show run") 
print(output)

net_connect.disconnect()
