from napalm import get_network_driver

driver = get_network_driver('ios')
router = driver('10.1.1.3', 'ccnp', 'cisco')
router.open()

print('Accessing R1 : 10.1.1.3')

cmds = [
    'interface l0',
    'ip add 1.1.1.1 255.255.255.0'
]

config_str = '\n'.join(cmds)

router.load_merge_candidate(config=config_str)

router.commit_config()

output = router.get_config()

print(output)

router.close()