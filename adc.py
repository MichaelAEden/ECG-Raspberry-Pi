#!/usr/bin/python

# Taken from: https://github.com/pimylifeup/Pi-ADC-Example-Code/blob/master/adc-code.py

import spidev
import time

# Define Variables.
delay = 0.5
channel = 0


def readadc(adcnum):
    # Read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data


def run():
    #C reate SPI.
    spi = spidev.SpiDev()
    spi.open(0, 0)

    # Read values from channel.
    while True:
        ldr_value = readadc(channel)
        print "---------------------------------------"
        print("LDR Value: %d" % ldr_value)
        time.sleep(delay)


if __name__ == '__main__':
    main()
