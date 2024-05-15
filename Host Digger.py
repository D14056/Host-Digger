import os
import subprocess
import socket
import ssl
from colorama import Fore, Back, Style
import time

# ASCII art for "Dinelka"
print("""
     ______   __   __  ______
    /      \ /  \ /  \/      \
   /$$$$$$|$$  |$$  |$$$$$$$
   $$ |  $$ | $$  | $$ |  $$
   $$ |  $$ | $$  | $$ |  $$
   $$ |  $$ | $$$$$$$$ |  $$
   $$/   $$/  $$/   $$/   $$/

""")
time.sleep(2)

def ping_host(ip, timeout):
    response = os.system(f"ping -c 1 -W {timeout} {ip} > /dev/null")
    if response == 0:
        print(Fore.GREEN + f"IP {ip} is working: ", end="")
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            print(f"{hostname}")
            with socket.create_connection((ip, 443), timeout=timeout) as sock:
                with ssl.create_default_context().wrap_socket(sock, server_hostname=hostname) as ssock:
                    print(Fore.GREEN + f"SSL/TLS handshake successful: {ssock.version()}")
                    return True
        except ConnectionRefusedError:
            print(Fore.RED + "SSL/TLS handshake failed: Connection refused")
            return False
        except Exception as e:
            print(Fore.RED + f"{e}")
            return False
    else:
        print(Fore.RED + f"IP {ip} is not working")
        return False

def ping_range(start_ip, end_ip, timeout):
    working_ips = []
    for ip in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
        current_ip = f"{start_ip.rsplit('.', 1)[0]}.{ip}"
        if ping_host(current_ip, timeout):
            working_ips.append(current_ip)
        else:
            # Clear the line after printing "IP x.x.x.x is not working"
            print("\033[F\033[K", end="")
    print(Fore.GREEN + "Working IPs: ", working_ips)

# Prompt the user to enter the start IP, end IP, and ping timeout
start_ip = input("Enter the start IP: ")
end_ip = input("Enter the end IP: ")
timeout = input("Enter the ping timeout (in seconds): ")

# Call the ping_range function with the user-provided inputs
ping_range(start_ip, end_ip, int(timeout))
