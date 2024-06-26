#Ubuntu To R1
#라우터에 접속하여 루프백 인터페이스를 생성하고 조회하는 파이썬 자동화 코드를 완성하시오.
import getpass  # 필요한 라이브러리 임포트
import telnetlib

HOST = "10.1.1.21"  # 텔넷 서버 호스트 주소 설정
user = input("Enter your telnet username: ")  # 사용자 원격 계정 입력 받음
password = getpass.getpass()  # 사용자에게 비밀번호 입력을 요청할 때 "Password: "라는 프롬프트가 화면에 표시

#password = getpass.getpass("Enter your telnet password: ") 사용자에게 "Enter your telnet password: "라고 표시

tn = telnetlib.Telnet(HOST)  # 지정된 호스트로 텔넷 연결 시작

# 바이트 타입 데이터 : 주로 파일 입출력, 네트워크 통신, 바이너리 데이터 처리 등에서 사용
# ASCII 인코딩 : string 타입 → byte 타입 
# string <-> byte(ascii) <-> string

tn.read_until(b"Username: ")  # 사용자 이름 입력 대기
tn.write(user.encode('ascii') + b"\n")  # 사용자 이름 전송
if password:
    tn.read_until(b"Password: ")  # 비밀번호 입력 대기
    tn.write(password.encode('ascii') + b"\n")  # 비밀번호 전송

tn.write(b"sh ip int br\n")
tn.write(b"conf t\n")
tn.write(b"int l0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"sh ip int br\n")
tn.write(b"exit\n") # 텔넷 세션 종료

print(tn.read_all().decode('ascii')) # 텔넷 세션 출력 읽고 디코드하여 출력
