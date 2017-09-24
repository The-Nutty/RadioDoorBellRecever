#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


radio = RFM69.RFM69(RF69_868MHZ, 1, 1, True)
print "class initialized"
#set frequency deviation VERY SLIGTLY MORE, DOES THIS MATTER?
radio.writeReg(0x05, 0x3)#most significant bit
radio.writeReg(0x06, 0xDF)#least significant bit

radio.setFreqeuncy(14226083)#IS GOOD

# # #set baud rate to 20
# radio.writeReg(0x03, 0x4)#most significant bit
# radio.writeReg(0x04, 0x2)#least significant bit
#set baud rate to 5k7
radio.writeReg(0x03, 0x15)#most significant bit
radio.writeReg(0x04, 0xEE)#least significant bit
print "set baud rate"


print "Performing rcCalibration"
radio.rcCalibration()
print "setting high power"
radio.setHighPower(True)

print "sending blah to 2"

for i in  range(30):
    radio.send(1, bitstring_to_bytes("010101010101010101010101001011011101010010000000000000000000110000000101011010"))
    time.sleep(0.015)

print "shutting down"
radio.shutdown()

# todo check if works using rtl-sdr then see if does anything to boiler