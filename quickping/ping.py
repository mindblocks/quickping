import time
import random
import struct
import select
import socket


def chk(data):
    x = sum(x << 8 if i % 2 else x for i, x in enumerate(data)) & 0xFFFFFFFF
    x = (x >> 16) + (x & 0xFFFF)
    x = (x >> 16) + (x & 0xFFFF)
    return struct.pack('<H', ~x & 0xFFFF)


def ping(addr, timeout=1, number=1, data=b''):
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as connection:

        payload = struct.pack('!HH', random.randrange(0, 65536), number) + data
        connection.connect((addr, 80))

        connection.sendall(b'\x08\0' + chk(b'\x08\0\0\0' + payload) + payload)

        start = time.time()

        while select.select([connection], [], [], max(0, start + timeout - time.time()))[0]:
            data = connection.recv(65536)
            if len(data) < 20 or len(data) < struct.unpack_from('!xxH', data)[0]:
                continue
            if data[20:] == b'\0\0' + chk(b'\0\0\0\0' + payload) + payload:
                return True
        return False

