# Ubuntu To All Devices
# 모든 장비들의 running-config 파일 파일로 백업하는 파이썬 자동화 코드를 완성하시오.
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f=open('myswitches')

for IP in f:
    IP=IP.strip()
    print('Get running Config from Switch ' + IP)
    tn = telnetlib.Telnet(IP)
    #사용자 이름 입력
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    #비밀 번호 입력
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    #명령어 연속 실행
    tn.write(b"terminal length 0\nsh run\nexit\n")
    #출력을 읽음
    readoutput = tn.read_all()
    #출력을 파일에 저장
    saveoutput = open('switch' + IP,'w')
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close()
