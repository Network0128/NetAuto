from netmiko import ConnectHandler 

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="10.1.1.21",
    username="ccnp",
    password="cisco"
)

#send_command: 관리자 모드의 명령어를 보내는데 사용
print(net_connect.send_command("show ip int brief"))
print(net_connect.send_command("show run"))

net_connect.disconnect()
