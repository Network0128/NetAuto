#Ubuntu To multiple switch
#가독성을 높이기 위해 telnet5.py를 수정(with문 사용)
import telnetlib

user, password = "ccnp", "cisco"

with open('all_devices') as f: (with 구문 사용으로 자동 close)
    for IP in f:
        IP = IP.strip()
        print(f'Get running Config from Device {IP}')
        # Telnet 연결 및 명령어 실행 (with 구문 사용으로 자동 close)
        with telnetlib.Telnet(IP) as tn: 
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"terminal length 0\nsh run\nexit\n")
    
            # 출력을 파일에 저장 (with 구문 사용으로 자동 close)
            with open(f'device_{IP}', 'w') as save:
                save.write(tn.read_all().decode('ascii'))           
