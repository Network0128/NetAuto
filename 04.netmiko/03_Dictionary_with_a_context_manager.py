from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco"
}

# Will automatically 'disconnect()' -> 'ConnectHandler'를 컨텍스트 매니저로 사용하여 자동 연결 해제를 보장

with ConnectHandler(**router1) as net_connect:  
    print(net_connect.find_prompt()) # 장비의 명령 프롬프트를 출력하여 연결 확인
    output = net_connect.send_command("show ip int brief")  # 장비에 명령을 보내고 출력을 저장
    print(output)  # 명령의 출력을 출력

--------------------------------------------------------------
#위의 코드와 동일, 명령어를 변수에 저장
command="show ip int brief"

with ConnectHandler(**router1) as net_connect:
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    print(output)
--------------------------------------------------------------
#위의 코드와 동일, 여러 명령어를 리스트에 저장
commands=["show ip int brief",'show run']

for cmd in commands:
    with ConnectHandler(**router1) as net_connect:
        print(net_connect.find_prompt())
        output = net_connect.send_command(cmd)
        print(output)
