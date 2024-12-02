# Ubuntu To multiple switch
#접속 대상 장비들을 파일로 만들어서 반복문과 함께 실행하는 파이썬 자동화 코드를 완성하시오.
import telnetlib

user = 'ccnp'
password = 'cisco'

f = open('myswitches') #relative Path : 파일을 못찾는 경우 해당 파일이 있는 디렉터리로 이동 후 실행
#Absolute Path : f = open('/home/ubuntu/PythonHome/1.telnet/myswitches')

for IP in f:
    IP = IP.strip()
    print('Configuring Switch ' + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

----------------------------
# 파일을 사용하지 않을 경우 : 실습 - 1
myswitches = ("10.1.1.11","10.1.1.12","10.1.1.13")
#list, tuple, set, dictionary 모두 가능 주로 불변성의 튜플 사용
for HOST in myswitches:
    print("지금 접속 장비의 IP : ", HOST)
    for n in range(2,11):
        print("vlan " + str(n),end='\n')
        print("name Python_VLAN_" + str(n))  
    print() 
----------------------------
# 파일을 사용하지 않을 경우 : 실습 - 2
import telnetlib
user = "ccnp"
password = "cisco"

myswitches = ("10.1.1.11","10.1.1.12","10.1.1.13")
for IP in myswitches:
    print("Switch's IP address :", IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"sh vlan br\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))



