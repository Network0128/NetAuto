# Ubuntu To All Devices
# 모든 장비들의 running-config파일을 백업받는 파이썬 자동화 코드를 완성하시오.
import telnetlib

user = "ccnp"
password = "cisco"

f=open('all_devices') #python실행시 해당 파일하고 같은 디텍터리에서 실행해야함
#혹은 절대 경로 사용: f=open('/home/ubuntu/PythonHome/all_devices')

for IP in f:
    IP=IP.strip()
    print(f'Get running Config from Device {IP}')
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    #명령어 연속 실행
    tn.write(b"terminal length 0\nsh run\nexit\n")
    #출력을 읽어서 파일에 저장
    save_output = open(f'device_{IP}','w')  # f-string을 사용하여 IP 주소별 파일명 생성, 쓰기 모드로 파일 열기
    save_output.write(tn.read_all().decode('ascii')) # telnet 세션의 출력(bytes)을 ASCII 문자열로 디코딩하여 파일에 저장
    save_output.close()
