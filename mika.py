#!/usr/bin/python

# importing modules
import subprocess
import re
import random as r
from argparse import ArgumentParser  # install it using "pip install argparse"
from logo import logo


# creating a function to capture the arguments and options entered by the user in the terminal. And also checking whether the user entered arguments are right or not.
def get_argument():
    parser = ArgumentParser(description="----- A simple and powerful MAC changer tool -----", prog="python3 mika.py")
    parser.add_argument("-i", dest="interface", help="Specify the name of interface")
    parser.add_argument("-m", dest="new_mac", help="Specify a new mac or type 'r' to set random MAC Address insted of new mac")
    args = parser.parse_args()

    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")

    return args


# Creating a function for capturing current mac address. 
def get_mac(interface):
    interface_info = str(subprocess.run(["sudo", "ifconfig", interface], capture_output=True))
    interface_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface_info)
    return interface_mac.group(0)


# printing the logo
print(logo)

# capturing the option entered with arguments in terminal. 
arg = get_argument()
interface = arg.interface
new_mac = arg.new_mac

# generating a random mac address. 
if new_mac == "r":
    x = r.randint(0, 9)
    y = r.randint(0, 9)
    z = r.randint(0, 9)
    new_mac = f"00:{x}{y}:{y}{z}:{z}{x}:{y}{x}:{z}{y}"

# capturing the current mac address. 
current_mac = get_mac(interface)

# executing the kali linux terminal commands for changing the mac address. 
subprocess.run(["sudo", "ifconfig", interface, "down"])
subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["sudo", "ifconfig", interface, "up"])

# capturing the changed mac address. 
changed_mac = get_mac(interface)

# Showing whether your mac address has changed or not.
if current_mac != changed_mac:
    print(f'Now, Your MAC for "{interface}" is successfully change from "{current_mac}" to "{changed_mac}"\n')
else:
    print("Try Again!!!\n")
