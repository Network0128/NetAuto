#Ubuntu To SW1 : Using loop
#반복문을 활용하여 VLAN을 생성하는 파이썬 자동화 코드를 완성하시오.
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

tn.write(b"conf t\n")
for n in range(2, 11):  # 2부터 10까지 반복
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")  # VLAN 구성 명령어 전송
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")  # VLAN 이름 설정 명령어 전송

tn.write(b"end\n")
tn.write(b"sh vl br\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
