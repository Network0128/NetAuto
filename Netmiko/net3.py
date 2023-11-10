from netmiko import ConnectHandler

switch1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.11',
    'username': 'ccnp',
    'password': 'cisco'
}

switch2 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.12',
    'username': 'ccnp',
    'password': 'cisco'
}

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.13',
    'username': 'ccnp',
    'password': 'cisco'
}

with open('switch_design') as f:
    lines = f.read().splitlines()
print(lines)

devices = [switch1, switch2, switch3]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print(output)
