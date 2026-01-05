깔끔한 실습을 위해 각 장비에서 배너 off
conf t
no banner motd
no banner login
no banner exec
end
wr


#Ubuntu To R1
#라우터에 접속하여 루프백 인터페이스를 생성하고 조회하는 파이썬 자동화 코드를 완성하시오.
import getpass  # 필요한 라이브러리 임포트
import telnetlib

HOST = "10.1.1.21"  # 텔넷 서버 호스트 주소 설정
username = input("Enter your telnet username: ")  # 사용자 원격 계정 입력 받음
password = getpass.getpass()  # 사용자에게 비밀번호 입력을 요청할 때 "Password: "라는 프롬프트가 화면에 표시

#password = getpass.getpass("Enter your telnet password: ") 사용자에게 "Enter your telnet password: "라고 표시

tn = telnetlib.Telnet(HOST)  # 지정된 호스트로 텔넷 연결 시작

tn.read_until(b"Username: ")  # 사용자 이름 입력 대기
tn.write(username.encode('ascii') + b"\n")  # 사용자 이름 전송
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

# 바이트 타입 데이터: 주로 파일 입출력, 네트워크 통신, 바이너리 데이터 처리 등에서 사용된다.
# ASCII,UTF-8 인코딩: string 타입의 데이터를 byte 타입으로 변환할 때 사용되는 인코딩 방식 중 하나다.
# string(str,보통 유니코드) <-> byte(ASCII/UTF-8) <-> string(str,보통 유니코드)
   -> Python 3에서 str 타입은 내부적으로 유니코드 문자열을 표현한다. 따라서 보통은 "문자열 = 유니코드 문자열"이 맞지만, 모든 언어에서 string이 곧 유니코드라는 보장은 없다. (예: C의 char*는 단순 바이트 배열일 뿐, 유니코드 아님)
# ASCII나 UTF-8 같은 인코딩 방식을 사용하여 문자열을 바이트로 변환하고, 다시 문자열로 복원할 수 있다.

# ASCII 인코딩/디코딩
s = "hello"
b = s.encode('ascii')       # string -> byte (ASCII 인코딩)
print(b)  # 출력: b'hello'
s_back = b.decode('ascii')  # byte -> string (ASCII 디코딩)
print(s_back)  # hello

# UTF-8 인코딩/디코딩
s_utf8 = "안녕하세요"
b_utf8 = s_utf8.encode('utf-8')        # string -> byte (UTF-8 인코딩)
print(b_utf8)  # 출력: b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
s_back_utf8 = b_utf8.decode('utf-8')   # byte -> string (UTF-8 디코딩)
print(s_back_utf8)  # 출력: 안녕하세요

-----------------유니코드와 유니코드가 아닌 문자열 비교(파이썬 기본이 유니코드)----------------------------------------
1. 유니코드 문자열
정의: 전 세계의 문자(한글, 한자, 이모지, 알파벳, 아랍 문자 등)를 하나의 통합 코드 체계(Unicode Code Point) 로 표현한 문자열
특징
문자마다 고유한 번호(코드 포인트, 예: U+AC00 = "가")가 부여됨
저장할 때는 UTF-8, UTF-16, UTF-32 같은 인코딩 방식을 사용해 바이트로 변환해야 함

Python 3의 str 타입은 바로 이 유니코드 문자열을 다룸
장점
한글, 영어, 일본어, 이모지까지 모두 같은 방식으로 처리 가능
다국어 지원이 가능 → 웹, DB, 국제 서비스 필수

2. 유니코드가 아닌 문자열 (바이트 기반)
정의: 특정 문자 집합(ASCII, EUC-KR, Shift-JIS 등)에 따라 직접 바이트 값과 문자를 매핑하는 방식
특징
예: ASCII
1바이트 = 1문자 (0~127)
A → 0x41
한글/이모지 표현 불가



