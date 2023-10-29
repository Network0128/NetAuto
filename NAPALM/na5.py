from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.1.1.11', 'david', 'cisco')
iosvl2.open()

print ('Accessing 10.1.1.11')
iosvl2.load_merge_candidate(filename='ACL1.cfg')
iosvl2.commit_config()
iosvl2.close()
