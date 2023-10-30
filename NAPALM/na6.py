from napalm import get_network_driver

driver = get_network_driver('ios')
router1 = driver('10.1.1.3', 'ccnp', 'cisco')
router1.open()

print('Accessing 10.1.1.3')
router1.load_merge_candidate(filename='Merge1.cfg')

diffs = router1.compare_config()
if len(diffs) > 0:
    print(diffs)
    router1.commit_config()
else:
    print('No changes required.')
    router1.discard_config()

router1.close()
