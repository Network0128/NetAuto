#Ubuntu To SW1
#스위치에 접속하여 VLAN을 생성하고 조회하는 파이썬 자동화 코드를 완성하시오.
import getpass
import telnetlib

HOST = "10.1.1.11"
user = "ccnp"  # 사전에 정의된 사용자 이름
password = "cisco"  # 사전에 정의된 비밀번호

tn = telnetlib.Telnet(HOST) # 지정된 호스트로 텔넷 연결 시작

# 사용자 이름과 비밀번호를 자동으로 전송
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# 텔넷 세션을 통해 네트워크 명령 실행
tn.write(b"sh vlan br\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"end\n")
tn.write(b"sh vlan br\n")
tn.write(b"exit\n")

# 텔넷 세션의 모든 출력을 읽고 디코드하여 출력
print(tn.read_all().decode('ascii'))
