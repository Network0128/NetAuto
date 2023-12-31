#Ubuntu To multiple switch
#가독성을 높이기 위해 telnet5.py를 수정(with문 사용)
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass("Enter your telnet password: ")

# 'myswitches' 파일 오픈
with open('myswitches') as f:
    # 파일의 각 줄을 아래와 같이 반복
    for IP in f:
        IP = IP.strip()
        # f-string 문자열 포매팅 방식 : 문자열 내에 중괄호 {}를 사용해 변수나 표현식을 직접 삽입
        print(f'Get running Config from Switch {IP}')
        
        tn = telnetlib.Telnet(IP)
        
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        
        tn.write(b"terminal length 0\nsh run\nexit\n")
        
        readoutput = tn.read_all()
        
        # 출력을 파일에 저장
        with open(f'switch{IP}', 'w') as saveoutput:
            saveoutput.write(readoutput.decode('ascii'))
            saveoutput.write('\n')
