telnet 10.1.1.0 255.255.255.0 inside
aaa authentication telnet console LOCAL
aaa authorization exec LOCAL auto-enable


우분투에서 방화벽을 대상으로 각종 정보를 조회하는 코드

import telnetlib

IP = "10.1.1.31"
username = "ccnp"
password = "cisco"

tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal pager 0\n")
tn.write(b"show route\n")      ← sh int ip br/ sh run 도 실습(학원PC에서는 성공)
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

---
# 위의 코드가 실행이 안될 경우, 아래와 같이 \r\n 을 사용한다.

import telnetlib

IP = "10.1.1.31"
user = "ccnp"
password = "cisco"

# 1. 연결 설정 (타임아웃 추가)
tn = telnetlib.Telnet(IP, timeout=10)

# [Tip] 접속 직후 엔터 전송 (장비 깨우기) 생략 가능
# tn.write(b"\r\n")

# 2. 로그인 절차 (개행문자 \r\n 적용)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\r\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\r\n")

# 3. 로그인 직후 프롬프트(#) 청소
# 이 과정이 없으면 뒤에 오는 명령어 실행 결과가 꼬일 수 있음
tn.read_until(b"#")

# 4. 페이징 끄기 (긴 라우팅 테이블이 한 번에 나오도록)
tn.write(b"terminal pager 0\r\n")
tn.read_until(b"#")

# 5. 각종 조회 명령어 실행: sh int ip br, sh route, show run 등 가능
print("정보를 가져오는 중입니다...")
tn.write(b"show run\r\n")

# 6. 결과 읽기 (다음 프롬프트 #이 나올 때까지의 모든 내용을 저장)
route_output = tn.read_until(b"#")

# 7. 접속 종료
tn.write(b"exit\r\n")

# 8. 결과 출력 (bytes -> string 디코딩)
print("-" * 50)
print(route_output.decode('ascii'))
print("-" * 50)

------------------------------
