from netmiko import ConnectHandler  # Netmiko 라이브러리를 사용하여 네트워크 장비와 SSH 연결

# 네트워크 장비 연결 설정
net_connect = ConnectHandler(
    device_type="cisco_ios",  # Cisco IOS 장비 타입 설정
    host="10.1.1.21",        # 장비의 IP 주소
    username="ccnp",         # 장비 접속 사용자 이름
    password="cisco"         # 장비 접속 비밀번호
)

# send_command: 관리자 모드의 명령어를 보내는데 사용, 아래 명령어를 차례대로 실행 해보자.
print(net_connect.send_command("show ip int brief"))  # 인터페이스 상태 요약 출력
print(net_connect.send_command("show run"))          # 실행 중인 설정 출력

net_connect.disconnect()  # 연결 종료

