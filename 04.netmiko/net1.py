# SW1 접속 : show ip int br 확인, loopback 0에 ip 설정, vlan 설정

from netmiko import ConnectHandler  #netmiko 모듈에서 ConnectHandler 클래스를 가져와서 사용

switch1 = {  # 스위치 연결 파라미터 정의
    'device_type': 'cisco_ios',  # Netmiko가 올바른 디바이스 클래스를 사용하도록 디바이스 타입 지정
    'ip': '10.1.1.11',   # 스위치의 IP 주소, ConnectHandler 클래스에서는 ip 대신 host명도 가능
    'username': 'ccnp',  
    'password': 'cisco'  
}

net_connect = ConnectHandler(**switch1)  # 스위치와 연결 : switch1 딕셔너리를 ConnectHandler 클래스의 인자로 사용하여 net_connect 객체를 만듭니다.

output = net_connect.send_command('show ip int brief')  #net_connect 객체를 사용하여 show ip int brief 명령어를 실행
print(output)  # 결과 출력

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']  # 리스트에 명령어 2개 포함
output = net_connect.send_config_set(config_commands)  # 설정 변경 명령어를 스위치에 전송
print(output)  # 결과 출력

for n in range(2, 11):  # VLAN 2부터 10까지 생성하기 위한 반복문
    print("Creating VLAN " + str(n))  # VLAN 생성 중임을 나타내는 메시지 출력
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]  # VLAN을 생성하고 이름을 지정하는 명령어 정의
    output = net_connect.send_config_set(config_commands)  # VLAN 설정 명령어를 스위치에 전송
    print(output)  # 결과 출력

-----------------with 문으로 처리------------------

from netmiko import ConnectHandler

SW1 = {
    "device_type" : "cisco_ios",
    "host" : "10.1.1.11",
    "username" : "ccnp",
    "password" : "cisco",
    "global_delay_factor": 2,
}
commands=["int loopback 0","ip add 2.2.2.2 255.255.255.0"]

with ConnectHandler(**SW1) as net_connect:
    print(net_connect.find_prompt())
    print(net_connect.send_config_set(commands))
    print(net_connect.send_command("show ip int br"))
    for n in range(2,11):
        config_commands = ["vlan "+str(n),"name Python_VLAN "+ str(n)]
        print(net_connect.send_config_set(config_commands))
    print(net_connect.send_command("show vlan br"))
    
    




