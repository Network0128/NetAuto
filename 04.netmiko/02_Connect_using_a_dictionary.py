from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
}

net_connect = ConnectHandler(**router1) # **router1 : 딕셔너리의 각 키-값 쌍이 함수의 인자로 전달

print(net_connect.send_command("show ip int brief"))
print(net_connect.send_command("show run"))

net_connect.disconnect()
