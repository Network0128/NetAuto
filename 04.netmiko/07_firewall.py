ASA를 Netmiko 자동화 대상에 추가
from netmiko import ConnectHandler

firewall = {
    "device_type": "cisco_asa",
    "host": "10.1.1.31",
    "username": "ccnp",
    "password": "cisco",
}

net_connect = ConnectHandler(**firewall) 
#명령어를 차례대로 하나씩 실행해보자
#print(net_connect.send_command("show int ip brief")) 
#print(net_connect.send_command("show route")) 
print(net_connect.send_command("show run")) 
net_connect.disconnect()

-------------------------
with as 구문으로 수정

from netmiko import ConnectHandler
firewall = {
    "device_type":"cisco_asa",
    "host":"10.1.1.31",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2, #모든 지연 시간을 2배로 증가시킨다.
}

with ConnectHandler(**firewall) as net_connect:
    print(net_connect.find_prompt())
    print(net_connect.send_command("sh route"))
    print(net_connect.send_command("sh run"))

-------------------------
running config 를 파일로 저장

from netmiko import ConnectHandler
firewall = {
    "device_type":"cisco_asa",
    "host":"10.1.1.31",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2, 
}

with ConnectHandler(**firewall) as net_connect:
    running_config = net_connect.send_command("sh run")
    with open(f'device_{firewall["host"]}','w') as f:
        f.write(running_config)

-------------------------
모든 장비의 running config를 파일로 저장

from netmiko import ConnectHandler
firewall = {
    "device_type":"cisco_asa",
    "host":"10.1.1.31",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2, 
}
router1 = {
    "device_type":"cisco_ios",
    "host":"10.1.1.21",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2, 
}
router2 = {
    "device_type":"cisco_ios",
    "host":"10.1.1.22",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2,
}
switch1 = {
    "device_type":"cisco_ios",
    "host":"10.1.1.11",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2,
}
switch2 = {
    "device_type":"cisco_ios",
    "host":"10.1.1.12",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2,
}
switch3 = {
    "device_type":"cisco_ios",
    "host":"10.1.1.13",
    "username":"ccnp",
    "password":"cisco",
    "global_delay_factor": 2,
}

for device in (firewall,router1,router2,switch1,switch2,switch3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        print("Saving the 'Show run'output to File")
        running_config = net_connect.send_command("sh run")
        with open(f'device_{device["host"]}','w') as f:
            f.write(running_config)

print("All tasks Completed!!")

----------

