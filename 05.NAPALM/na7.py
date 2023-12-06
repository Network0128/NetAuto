from napalm import get_network_driver
driver = get_network_driver('ios')
switch2 = driver('10.1.1.12', 'ccnp', 'cisco')
switch2.open()

print('Accessing 10.1.1.12')
switch2.load_merge_candidate(filename='Merge1.cfg')

diffs = switch2.compare_config()
if len(diffs) > 0:
    print(diffs)
    switch2.commit_config()
else:
    print('No change : ACL, loopback')
    switch2.discard_config()

switch2.load_merge_candidate(filename='ospf1.cfg')

diffs = switch2.compare_config()
if len(diffs) > 0:
    print(diffs)
    switch2.commit_config()
else:
    print('No change : OSPF')
    switch2.discard_config()

switch2.close()
