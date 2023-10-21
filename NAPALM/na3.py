import json

from napalm import get_network_driver

driver = get_network_driver('ios')

switch1 = driver('10.1.1.11', 'ccnp', 'cisco')

switch1.open()

output = switch1.get_facts()

print(json.dumps(output,indent=4))#4칸 들여쓰기 출력

switch1.close()