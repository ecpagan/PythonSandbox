import socket
import termcolor

# TODO: Receive a banner from the open ports and store result in a variable and print it out
# Banner is something that an open port might send as information as to which software it's running on that open port
# From that banner we can also extract the version of the software


def scan(target, ports):
    print(f'\nStarting Scan for {target}')
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f'[+]Port Opened {port}')
        sock.close()
    except:
        pass
        # print(f'[-]Port Closed {port}')


targets = input('[*] Enter targets to scan (split them by ,): ')
ports = int(input('[*] Enter how many ports you want to scan: '))

if ',' in targets:
    print(termcolor.colored('[*] Scanning multiple targets', 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
