from netmiko import ConnectHandler

NXOS1 = {
    'device_type': 'cisco_nxos',
    'ip': '10.1.1.20',
    'username': 'ccnp',
    'password': 'cisco123!'
}

net_connect = ConnectHandler(**NXOS1)
output = net_connect.send_command('show ip interface brief')
print(output)

config_commands = ['interface loopback0', 'ip address 1.1.1.1/24']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2, 11):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
