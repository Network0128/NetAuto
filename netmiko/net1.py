from netmiko import ConnectHandler

switch1 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.11',
    'username': 'ccnp',
    'password': 'cisco'
}

net_connect = ConnectHandler(**switch1)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2, 11):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
