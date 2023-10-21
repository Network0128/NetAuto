import socket
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')
switch1.open()

ip_address = socket.gethostbyname('google.com')
output = switch1.ping(ip_address) #주의

print(json.dumps(output,indent=4))
switch1.close()
