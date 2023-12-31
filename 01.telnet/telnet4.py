# Ubuntu To multiple switch
import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

#import os //relative Path : 1
#os.chdir('/home/ubuntu/PythonHome/1.telnet') //relative Path : 2
f = open('myswitches') #relative Path : 3

#Absolute Path 
#f = open('/home/ubuntu/PythonHome/1.telnet/myswitches')

for IP in f:
    IP = IP.strip()
    print('Configuring Switch ' + IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)
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
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
