
def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])
print int(bitstring_to_bytes("010101010101010101010101001011011101010010000000000000000000110000000101011010"))