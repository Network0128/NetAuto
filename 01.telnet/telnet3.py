#Ubuntu To SW1 : Using loop
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

tn.write(b"conf t\n")
for n in range (2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VALN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"sh vl br\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
