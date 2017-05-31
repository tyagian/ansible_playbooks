#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from getpass import getpass
from pprint import pprint

driver = get_network_driver('eos')
device = driver('eos', 
                username='anujtyagi',
                password=getpass())

print()
print(">>>Test device open")
device.open()
