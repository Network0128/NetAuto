# Ubuntu To All Devices
# 모든 장비들의 running-config파일을 백업받는 파이썬 자동화 코드를 완성하시오.
import telnetlib

user = "ccnp"
password = "cisco"

f=open('all_devices') #python실행시 해당 파일하고 같은 디텍터리에서 실행해야함
#혹은 절대 경로 사용: f=open('/home/ubuntu/PythonHome/all_devices')

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
    read_output = tn.read_all() #전체 Telnet 세션의 출력을 읽어서 'read_output' 변수에 저장
    #출력을 파일에 저장
    save_output = open('device_' + IP,'w') #파일 이름을 'device + IP'로 지정하고 쓰기 모드('w')로 파일을 연다.
    save_output.write(read_output.decode('ascii')) #'read_output'의 바이트열 형태를 문자열로 변환하여 파일에 작성
    save_output.close()
