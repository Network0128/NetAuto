# Cisco IOS 장비의 설정을 변경하고 저장하는 과정을 자동화합니다.
# send_config_set과 save_config 메소드를 통해 설정 파일을 변경하고, 저장합니다.

from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
}

commands = ["logging buffered 100000"] #라우터의 내부 로깅 버퍼 크기를 100,000바이트로 설정
with ConnectHandler(**router1) as net_connect:
    output = net_connect.send_config_set(commands) #send_config_set: 전역 설정 모드의 명령어를 보내는데 사용
    output += net_connect.save_config() #네트워크 장비의 현재 설정 저장

print()
print(output)
print()
#print(f"\n{output}\n")
