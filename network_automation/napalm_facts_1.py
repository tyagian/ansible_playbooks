#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from getpass import getpass
from pprint import pprint

device1 = {
    'hostname': '192.168.25.40', 
    'username': 'anujtyagi',
    'password': getpass(),
    'optional_args': {},
}

driver = get_network_driver('eos')
napalm_conn = driver(**device1)

print()
print(">>>Test device open")
napalm_conn.open()

pprint(napalm_conn.get_facts())
