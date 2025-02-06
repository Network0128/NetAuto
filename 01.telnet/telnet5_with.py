#Ubuntu To multiple switch
#가독성을 높이기 위해 telnet5.py를 수정(with문 사용)
import telnetlib

user = "ccnp"
password = "cisco"

# 'all_devices' 파일 오픈
with open('all_devices') as f:
    for IP in f:
        IP = IP.strip()
        print(f'Get running Config from Device {IP}')
        tn = telnetlib.Telnet(IP)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"terminal length 0\nsh run\nexit\n")
        read_output = tn.read_all()
        
        # 출력을 파일에 저장
        with open(f'device_{IP}', 'w') as save_output:
            save_output.write(read_output.decode('ascii'))           
