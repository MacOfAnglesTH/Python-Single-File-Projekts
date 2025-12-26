######################################################################################################
# This Python file creates a Netplan file with a static ip-address and set th new hostname
# Auto detect only a port plugged to the computer.
# @author Mac Müller
######################################################################################################
#################################### ONLY run with SUDO !! ###########################################
#################################### sudo python2 ~/init.py ##########################################

import netifaces
import ipaddress
import yaml
import subprocess
import time

if __name__ == "__main__":

    # Getting inputs
    print("hostname?")
    hostname = str(input())
    print("ip?")
    ip = str(input())
    print("prefix?")
    prefix = str(input())

    # Init dictionary object
    netplan = {
        "network": {
            "version": 2,
            "renderer": "networkd",
            "ethernets": {}
        }
    }

    # Define the fist ip-address as gateway
    ip_gateway = str(ipaddress.ip_network(ip+"/"+prefix, strict=False).network_address + 1)

    # Define the DNS IP address. In my case, we are running the edges in one of two networks
    ip_dns = "private.0.10.1" if ip.startswith("private.0.private99") else "private.220.61.3"

    # set all interface dhcp or write static ip address if link detected
    interfaces = netifaces.interfaces()
    interfaces.remove("lo")
    linkNotDetected = True
    while linkNotDetected:
        for i in interfaces:
            ps = subprocess.Popen("ethtool "+i+" | sed -n -e 's/^.*Link detected: //p'", stdout=subprocess.PIPE, text=True, shell=True)
            result = ps.communicate()
            print(i + ": " + result[0][:-1])
            if result[0] == "yes\n":
                    netplan["network"]["ethernets"][i] = {}
                    if_main = netplan["network"]["ethernets"][i]
                    if_main["addresses"] = "["+ip+"/"+prefix +"]"
                    if_main["routes"] = { "- to": "default", "  via": ip_gateway }
                    if_main["nameservers"] = { "search": "[ RSSLAB.local ]", "addresses": "[ "+ip_dns+" ]" }
                    linkNotDetected = False
            else:
                netplan["network"]["ethernets"][i] = { "dhcp4": "yes" }
        if linkNotDetected:
            print ("No plugged cabel detected: wait 5 seconds .....")
            time.sleep(5)

    # Writing to netplan-file
    with open("/etc/netplan/50-cloud-init.yaml", "w") as outfile:
        yaml.dump(netplan, outfile, default_style=None, default_flow_style=False, sort_keys=False)

    # Remove the apostrophes from YAML
    with open("/etc/netplan/50-cloud-init.yaml", "rt") as filein:
        netplan = filein.read().replace("'", "")
    with open("/etc/netplan/50-cloud-init.yaml", "w") as outfile:
        outfile.write(netplan)

    # Apply netplan
    subprocess.run(["netplan", "apply"])
    # Apply the new hostname
    subprocess.run(["hostnamectl", "set-hostname", hostname])
    # Reboot
    subprocess.run(["reboot", "now"])