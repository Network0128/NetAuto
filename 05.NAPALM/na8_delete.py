#모든 장비를 대상으로 직전의 설정을 취소한다.

from napalm import get_network_driver
import json  

devices = ['10.1.1.11','10.1.1.12','10.1.1.13','10.1.1.21', '10.1.1.22']

for ip_address in devices:
    print(f"Connecting to {ip_address}")
    driver = get_network_driver('ios')  
    device = driver(hostname=ip_address, username='ccnp', password='cisco') 
    device.open()  

    device.load_merge_candidate(filename='delete.cfg') 

    diffs = device.compare_config() 
    if len(diffs) > 0:
        print(diffs)
        device.commit_config()
    else:
        print('No changed')
        device.discard_config()

    device.close() 
