import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f=open('myswitches')

for IP in f:
    IP=IP.strip()
    print('Get running Config from Switch ' + IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"sh run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open('switch' + HOST,'w')
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close