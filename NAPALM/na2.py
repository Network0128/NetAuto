from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(hostname='10.1.1.3', username='ccnp', password='cisco')

device.open()

interfaces = device.get_interfaces()

print(interfaces)

device.close()