from decorators.track_time import exec_time
import os
from functools import lru_cache


print("Initiaiting script... (#FuckDNSWatch)")


@lru_cache  # Used to not allow the same search to be made in the same session of the script. To avoid overloading the logs file.
@exec_time  # Keeps logs of how fast each of the functions was executed. 
def dns_check_NS(dom):
    print()
    print("NS records: ")
    return os.system(f"dig +short NS {dom}")


@lru_cache
@exec_time
def dns_check_A(dom):
    print()
    print("A and cName records: ")
    return os.system(f"dig +short A {dom}; dig +short A www.{dom}; dig +short cName www.{dom}; dig +short AAAA {dom}")


@lru_cache
@exec_time
def dns_check_mx(dom):
    print()
    print("MX records: ")
    return os.system(f"dig +short MX {dom}")
    

@lru_cache
@exec_time
def dns_check_txt(dom):
    print()
    print("TXT records: ")
    return os.system(f"dig +short TXT {dom}")


@lru_cache
@exec_time
def dns_check_dnssec(dom):
    print()
    print("DNSSEC records: ")
    return os.system(f"whois {dom} | grep -i dnssec")
    

domain = input("Please add the domain you wish to use: ")

dns_check_NS(domain)
dns_check_A(domain)
dns_check_mx(domain)
dns_check_txt(domain)
dns_check_dnssec(domain)

print()
user_input = input("Would you like to keep the script opened?\n Yes / No\n ")
print()

while user_input == "Yes" or user_input == "y" or user_input == "yes":
    domain = input("Please add the domain you wish to use: ")
    
    dns_check_NS(domain)
    dns_check_A(domain)
    dns_check_mx(domain)
    dns_check_txt(domain)
    dns_check_dnssec(domain)
    
    print()
    user_input = input("Would you like to keep the script opened?\n Yes/ No\n ")
    print()

if user_input == "No" or user_input == "n" or user_input == "no":
    print("Closing script ... ")
    print("Script closed. ")
    
else:
    print("Invalid input.\nClosing script. ")
