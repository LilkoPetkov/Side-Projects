import os
def hosts_file_add(domain, IP):
    return os.system(f"echo '{IP} {domain} www.{domain}' >> /etc/hosts")


def show_hosts_file():
    return os.system(f"tail -5 /etc/hosts")
  

def hosts_file_remove(domain):
    return os.system(f'echo "$(grep -v "{domain}" /etc/hosts)" > /etc/hosts')
    

def ping_check(domain):
    return os.system(f"ping -c3 {domain}")


domain = input("Please add domain: ")
IP = input("Please add IP for the domain: ")

print("Initialising hosts file script... ")

hosts_file_add(domain, IP)

print("Hosts file contents: ")

show_hosts_file()

user_input_0 = input("Would you like to perform a ping test? Yes/No \n")

if user_input_0 == "Yes" or user_input_0 == "y" or user_input == "yes":
    ping_check(domain)

user_input = input("Would you like to delete the domain from the hosts file? Yes/No \n")

if user_input == "Yes" or user_input == "y" or user_input == "yes":
    hosts_file_remove(domain)
    print("Entry removed from the hosts file. ")
    
    show_hosts_file()

print("Closing script. ")
