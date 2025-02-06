#Ubuntu To multiple switch
#가독성을 높이기 위해 telnet5.py를 수정(with문 사용)
import telnetlib

user, password = "ccnp", "cisco"

# 'all_devices' 파일을 열어 IP 목록을 읽음
with open('all_devices') as f:
    for IP in f:
        IP = IP.strip()
        print(f'Get running Config from Device {IP}')
        # Telnet 연결 및 명령어 실행
        with telnetlib.Telnet(IP) as tn: #tn.close()를 명시적으로 호출할 필요가 없이, 연결이 끝나면 자동으로 닫힘
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"terminal length 0\nsh run\nexit\n")
    
            # 출력을 파일에 저장
            with open(f'device_{IP}', 'w') as save_output:
                save_output.write(tn.read_all().decode('ascii'))           
