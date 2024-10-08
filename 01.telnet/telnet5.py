# Ubuntu To All Devices
# 모든 장비들의 running-config파일을 백업받는 파이썬 자동화 코드를 완성하시오.
import telnetlib

user = "ccnp"
password = "cisco"

f=open('all_devices') #python실행시 해당 파일하고 같은 디텍터리에서 실행해야함

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
    read_output = tn.read_all()
    #출력을 파일에 저장
    save_output = open('device' + IP,'w')
    save_output.write(read_output.decode('ascii'))
    save_output.write('\n')
    save_output.close()
