from napalm import get_network_driver

devices = ['10.1.1.11', '10.1.1.12', '10.1.1.13']

for ip_address in devices:
    print("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    switch = driver(ip_address, 'ccnp', 'cisco')
    switch.open()
    switch.load_merge_candidate(filename='Merge1.cfg')
    diffs = switch.compare_config()
    if len(diffs) > 0:
        print(diffs)
        switch.commit_config()
    else:
        print('No change : ACL, loopback')
        switch.discard_config()

    switch.load_merge_candidate(filename='ospf1.cfg')

    diffs = switch.compare_config()
    if len(diffs) > 0:
        print(diffs)
        switch.commit_config()
    else:
        print('No change : OSPF')
        switch.discard_config()

    switch.close()
