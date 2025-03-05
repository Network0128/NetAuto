# Netmiko 라이브러리를 사용하여 3개의 Cisco 스위치에 연결하고 VLAN 2부터 10까지 생성

from netmiko import ConnectHandler  

switch1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.11',  
    'username': 'ccnp', 
    'password': 'cisco'  
}

switch2 = {
    'device_type': 'cisco_ios', 
    'ip': '10.1.1.12',  
    'username': 'ccnp', 
    'password': 'cisco' 
}

switch3 = {
    'device_type': 'cisco_ios',  
    'ip': '10.1.1.13',  
    'username': 'ccnp', 
    'password': 'cisco' 
}

devices = [switch1, switch2, switch3]  

for device in devices:  # 각 스위치에 대해 반복
    net_connect = ConnectHandler(**device)  # 스위치에 연결
    for n in range(2, 11):  # VLAN 2부터 10까지 생성
        print("Creating VLAN " + str(n))  # 생성 중인 VLAN 번호 출력
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]  # VLAN 생성 및 이름 지정 명령어
        output = net_connect.send_config_set(config_commands)  # 명령어 실행 및 출력
        print(output)  # 결과 출력

---------------with 문으로 처리-------------

from netmiko import ConnectHandler

SW1 = {
    "device_type" : "cisco_ios",
    "host" : "10.1.1.11",
    "username" : "ccnp",
    "password" : "cisco",
    "global_delay_factor": 2,
}

SW2 = {
    "device_type" : "cisco_ios",
    "host" : "10.1.1.12",
    "username" : "ccnp",
    "password" : "cisco",
    "global_delay_factor": 2,
}

SW3 = {
    "device_type" : "cisco_ios",
    "host" : "10.1.1.13",
    "username" : "ccnp",
    "password" : "cisco",
    "global_delay_factor": 2,
}

for device in (SW1,SW2,SW3):
    with ConnectHandler(**device) as net_connect:
        print(net_connect.find_prompt())
        for n in range(2,11):
            config_commands = ["vlan "+str(n),"name Python_VLAN "+ str(n)]
            print(net_connect.send_config_set(config_commands))
        print(net_connect.send_command("show vlan br"))
    
    










