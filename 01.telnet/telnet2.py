#Ubuntu To SW1
#스위치에 접속하여 VLAN을 생성하고 조회하는 파이썬 자동화 코드를 완성하시오.
import getpass
import telnetlib

HOST = "10.1.1.11"
user = input("Enter your telnet username: ")
password = getpass.getpass("Enter your telnet password: ")

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh vlan br\n")
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
tn.write(b"sh vlan br\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
