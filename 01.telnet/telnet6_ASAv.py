telnet 10.1.1.0 255.255.255.0 inside
aaa authentication telnet console LOCAL
aaa authorization exec LOCAL auto-enable


import telnetlib

IP = "10.1.1.31"  # 텔넷 서버 호스트 주소 설정
user = "ccnp"  # 사전에 정의된 사용자 이름
password = "cisco"  # 사전에 정의된 비밀번호

tn = telnetlib.Telnet(IP)  # 지정된 호스트로 텔넷 연결 시작

# 사용자 이름과 비밀번호를 자동으로 전송
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

# 텔넷 세션을 통해 네트워크 명령 실행
tn.write(b"sh route\n")
tn.write(b"exit\n")  # 텔넷 세션 종료

# 텔넷 세션의 모든 출력을 읽고 디코드하여 출력
print(tn.read_all().decode('ascii'))

------------------------------
