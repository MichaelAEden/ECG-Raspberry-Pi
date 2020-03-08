#!/usr/bin/python

# Taken from: https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython

import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


SAMPLE_FREQ = 50.0
SAMPLE_PERIOD = 1 / SAMPLE_FREQ


def run():
    # Create SPI bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
     
    # Create CS (chip select)
    cs = digitalio.DigitalInOut(board.D5)
     
    # Create MCP object
    mcp = MCP.MCP3008(spi, cs)
     
    # Create analog input channel on pin 0
    channel = AnalogIn(mcp, MCP.P0)

    # TODO: determine how to sample at regular intervals.
    while True:
        # Note channel.value is a 16-bit integer, but the MCP is a 10-bit ADC.
        print('Raw ADC Value: ', channel.value)
        print('ADC Voltage: ' + str(channel.voltage) + 'V')
        time.sleep(SAMPLE_PERIOD)


if __name__ == '__main__':
    run()
