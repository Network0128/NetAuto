from napalm import get_network_driver
driver = get_network_driver('ios')
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')
switch1.open()

print('Accessing 10.1.1.11')
switch1.load_merge_candidate(filename='ACL1.cfg')
switch1.commit_config()
switch1.close()
