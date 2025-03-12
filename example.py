"""
Example script for PyEphEmber to dump various information from the API,
get the current temperature, and change the target temperature for a zone
"""
import argparse
from enum import Enum
import getpass
import json
import time

from pyephember.pyephember import EphEmber

from enum import IntEnum
from enum import auto

# global params

t = EphEmber("ad7ster@gmail.com", "W3Ar?sm0,,!dtK")

# Get the full home information
homes = t.get_homes()
print(json.dumps(homes, indent=4, sort_keys=True))
print("----------------------------------")

# Get only zone information
for home in homes:
    for zone in home["zones"]:
        print(json.dumps(zone, indent=4, sort_keys=True))

print("----------------------------------")

for name in t.get_zone_names():
    print(name)

# Get information about a zone
print("{} current temperature is {}".format(
    "zone_name", t.get_zone_temperature(args.zone_id)
))
print("{} target temperature is {}".format(
    "zone_name", t.get_zone_target_temperature(args.zone_id)
))
print("{} active : {}".format(
    "zone_name", t.is_zone_active(args.zone_id)
))
print("{} mode : {}".format(
    "zone_name", t.get_zone_mode(args.zone_id).name
))

#target = args.target
#if target is not None:
#    assert 0 <= target <= 25.5
#    t.set_zone_target_temperature(args.zone_name, target)
#    time.sleep(1)
#    print("{} target temperature changed to {}".format(
#        args.zone_name, t.get_zone_target_temperature(args.zone_name)
#    ))
#
#if args.advance is not None:
#    print("Setting advance for {} to {}".format(args.zone_name, args.advance))
#    if args.advance == 'on':
#        t.set_zone_advance(args.zone_name, True)
#    elif args.advance == 'off':
#        t.set_zone_advance(args.zone_name, False)
