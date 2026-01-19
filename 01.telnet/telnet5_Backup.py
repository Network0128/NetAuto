# Ubuntu To All Devices
# 모든 장비들의 running-config파일을 백업받는 파이썬 자동화 코드를 완성하시오.
import telnetlib

# 1. 설정 변수 (상단에서 일괄 관리)
USER = "ccnp"
PASSWORD = "cisco"
FILE_PREFIX = "backup_"   # 파일명 앞부분 (예: device_ -> backup_)
IP_LIST_FILE = "all_devices" # IP 리스트가 들어있는 파일명

# 2. 메인 로직
# 'with open'을 쓰면 close()를 안 해도 돼서 더 안전합니다.
try:
    with open(IP_LIST_FILE) as f:
        for IP in f:
            IP = IP.strip() # 공백/개행 제거
            if not IP: continue # 빈 줄이 있으면 건너뜀
            print(f'Get running Config from Device {IP}...')
            try:
                # 텔넷 접속
                tn = telnetlib.Telnet(IP, timeout=5) # 타임아웃 추가

                tn.read_until(b"Username: ")
                tn.write(USER.encode('ascii') + b"\n")
                
                tn.read_until(b"Password: ")
                tn.write(PASSWORD.encode('ascii') + b"\n")
                tn.write(b"terminal length 0\n") 
                tn.write(b"show running-config\n")
                tn.write(b"exit\n")

                # 3. 파일명 생성 및 저장 (변수 활용)
                # 최종 파일명 예시: backup_10.1.1.21.txt
                save_filename = f"{FILE_PREFIX}{IP}.txt"

                # 출력 내용 읽기
                output = tn.read_all().decode('ascii')

                # 파일 저장
                with open(save_filename, 'w') as save_file:
                    save_file.write(output)
                
                print(f" -> 저장 완료: {save_filename}")

            except Exception as e:
                print(f" -> {IP} 접속 실패: {e}")

except FileNotFoundError:
    print(f"[오류] '{IP_LIST_FILE}' 파일을 찾을 수 없습니다.")

------------
#스위치만 대상으로 불러오고, 파일로 백업을 할 경우

import telnetlib

#HOST = "10.1.1.11"
user = "ccnp"
password = "cisco"
myswitches=("10.1.1.11","10.1.1.12","10.1.1.13")  # <- 여러대의 스위치 목록들을 파일 단위로 관리
with open('myswitches') as f:
    for IP in f:
        IP=IP.strip()
        print("Switch's IP add: ",IP)
        tn = telnetlib.Telnet(IP)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"terminal length 0\n")
        tn.write(b"sh run\n")
        tn.write(b"exit\n")
        save=open(f'switch_{IP}','w')
        save.write(tn.read_all().decode('ascii'))
        save.close

