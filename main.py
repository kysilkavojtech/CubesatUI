import struct
import zlib


def human_print(B):
    print(' '.join('%02x' % b for b in B))


def get_sat_equatorial_command():
    header = bytearray(b'YU+')
    command_type = bytearray(b'R')
    command_code = (47).to_bytes(2, byteorder='big', signed=True)
    crc = bytearray((zlib.crc32(header + command_type + command_code)).to_bytes(8, byteorder='big', signed=True))
    cr = (13).to_bytes(1)
    return (header + command_type + command_code + crc + cr)

def get_sat_equatorial_response(response):
    if len(response) != 16 or response[:3] != bytearray(b'OK+') or response[15:] != (13).to_bytes(1):
        raise ValueError(f"The format of the response is incorrect.\n\tLength in bytes = {len(response)} (Expected: 16)\n\tHeader = {response[:3]} (Expected: {bytearray(b'OK+')})\n\tCR = {response[15:]} (Expected: {(13).to_bytes(1)})")
    x = struct.unpack('f', response[3:7])[0]
    y = struct.unpack('f', response[7:11])[0]
    z = struct.unpack('f', response[11:15])[0]
    return (x,y,z)

human_print(get_sat_equatorial_command())

valid_response = bytearray(b'OK+') + bytearray(struct.pack('f', 1.123)) + bytearray(struct.pack('f', 2.345)) + bytearray(struct.pack('f', 3.456)) + (13).to_bytes(1)
invalid_response_1 = bytearray(b'OK+') + bytearray(struct.pack('f', 1.123)) + bytearray(struct.pack('f', 2.345)) + bytearray(struct.pack('f', 3.456)) + (13).to_bytes(1) + bytearray(b'1')
invalid_response_2 = bytearray(b'ER+') + bytearray(struct.pack('f', 1.123)) + bytearray(struct.pack('f', 2.345)) + bytearray(struct.pack('f', 3.456)) + (13).to_bytes(1)
invalid_response_3 = bytearray(b'ER+') + bytearray(struct.pack('f', 1.123)) + bytearray(struct.pack('f', 2.345)) + bytearray(struct.pack('f', 3.456)) + bytearray(b'1')
# invalid_response_4 is only invalid because of the way it is constructed; it is converted without an error, so there should be a check for "reasonable numeric values"
invalid_response_4 = bytearray(b'OK+;;;;') + bytearray(struct.pack('f', 2.345)) + bytearray(struct.pack('f', 3.456)) + (13).to_bytes(1)


human_print(valid_response)
print(get_sat_equatorial_response(valid_response))