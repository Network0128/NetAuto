방화벽의 설정파일을 파일로 저장하시오.
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
tn.write(b"show run\n")
tn.write(b"exit\n")

#print(tn.read_all().decode('ascii'))
with open(f"devices_{IP}","w") as save:
    save.write(tn.read_all().decode('ascii'))

print(f"설정파일 저장완료: devices_{IP}")

--------------------------------------------
모든 장비의 설정 파일 백업

import telnetlib
username = "ccnp"
password = "cisco"

with open('mydevices') as file:
    for IP in file:
        IP = IP.strip()  
        print(f"지금 접속한 장비의 IP: {IP}")
        tn = telnetlib.Telnet(IP)
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        
        if IP == "10.1.1.31":
            print(" >> 방화벽(ASA) 감지: terminal pager 0 실행")
            tn.write(b"terminal pager 0\n")
        else:
            print(" >> 일반 장비(IOS) 감지: terminal length 0 실행")
            tn.write(b"terminal length 0\n")
        
        #tn.write(b"terminal length 0\n")
        tn.write(b"show run\n")
        tn.write(b"exit\n")
        #print(tn.read_all().decode('ascii'))
        with open(f"devices_{IP}","w") as save:
            save.write(tn.read_all().decode('ascii'))
        print(f"설정파일 저장완료: devices_{IP}")

---------------------------------------------
실행이 안될 경우, 아래 파일로 진행


import telnetlib

# 1. 설정 변수
IP = "10.1.1.31"
USER = "ccnp"
PASSWORD = "cisco"
FILENAME = f"backup_config_{IP}.txt"

print(f"[{IP}] 접속 및 백업 시작...")

try:
    # 2. 텔넷 연결 (타임아웃 10초)
    tn = telnetlib.Telnet(IP, timeout=10)

    # [Tip] 접속 직후 장비를 깨우기 위해 엔터 한 번 전송
    tn.write(b"\r\n")

    # 3. 로그인 절차
    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\r\n")

    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\r\n")

    # 4. 로그인 직후 프롬프트(#) 청소
    # 이것을 해야 뒤따르는 명령어들이 꼬이지 않습니다.
    tn.read_until(b"#")

    # 5. 페이징 비활성화 (한 번에 출력되도록 설정)
    tn.write(b"terminal pager 0\r\n")
    tn.read_until(b"#")

    # 6. 설정(Show Run) 가져오기
    tn.write(b"show running-config\r\n")
    
    # 다시 프롬프트(#)가 나올 때까지 모든 데이터 읽기
    read_data = tn.read_until(b"#")

    # 7. 접속 종료
    tn.write(b"exit\r\n")
    
    # 8. 파일 저장
    # read_data는 bytes 형식이므로 decode 필요
    with open(FILENAME, 'w') as f:
        f.write(read_data.decode('ascii'))

    print(f"[성공] 설정 파일이 '{FILENAME}'에 저장되었습니다.")

except Exception as e:
    print(f"[실패] 오류가 발생했습니다: {e}")
