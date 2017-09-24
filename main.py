import Spi as Spi

import RFM69
from RFM69registers import *
import datetime
import time


radio = RFM69.RFM69(RF69_868MHZ, 1, 1, True)
print "class initialized"

radio.setFreqeuncy()#frequency devided by 61.03507913
#see pages 63+ OF HERE http://www.hoperf.com/upload/rf/RFM69HW-V1.3.pdf

radio.writeReg(0x01, 10000100)#sequencer off, listen off, standby
radio.writeReg(0x02, 01001000)#continus with sync, OOK, no shaping


#set bit rate to 2k4
radio.writeReg(0x03, 0x34)#most significant bit
radio.writeReg(0x04, 0x15)#least significant bit

#0x19 needs to be set or left as defult?     /* 0x19 */ { REG_RXBW, RF_RXBW_DCCFREQ_010 | RF_RXBW_MANT_24 | RF_RXBW_EXP_4}, // BW: 10.4 kHz

radio.writeReg(0x1B, 01000000)#OOK threshold peack, 0.5db decremennts, one dec per chip
# radio.writeReg(0x1D, 6) this should not be needed as threshold type is peak
# radio.writeReg(0x29, 140) RSSI threshold in dBm = -(REG_RSSITHRESH / 2) this should not be needed as not sending anything
radio.writeReg(0x6F, 0x30)

#try change AfcAutoOn if bad stuff happens with frequency changing or Fei stuff

radio.setHighPower(True)
radio.setMode(RF69_MODE_STANDBY)

print "waiting for ready"
#wait for ready
while (radio.readReg(REG_IRQFLAGS1) & RF_IRQFLAGS1_MODEREADY) == 0x00:
    time.sleep(0.001)
print "ready"

print "looping"
while True:
    radio.receiveBegin()
    while not radio.receiveDone():
        time.sleep(0.01)

    print "%s from %s RSSI:%s" % ("".join([chr(letter) for letter in radio.DATA]), radio.SENDERID, radio.RSSI)