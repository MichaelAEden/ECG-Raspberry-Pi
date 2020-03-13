#!/usr/bin/python3

# Based on: https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython

import numpy as np
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import board
import busio
import digitalio
import random


class EcgCollector:

    def __init__(self, ch_pos, ch_neg, ch_gnd):
        # Create SPI bus
        self._spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
         
        # Create CS (chip select)
        self._cs = digitalio.DigitalInOut(board.D5)
         
        # Create MCP object
        self._mcp = MCP.MCP3008(self._spi, self._cs)

        # Initialize positive, negative, and ground channels.
        mcp_channels = [
            MCP.P0,
            MCP.P1,
            MCP.P2,
            MCP.P3,
            MCP.P4,
            MCP.P5,
            MCP.P6,
            MCP.P7
        ]
        self._ch_pos = AnalogIn(self._mcp, mcp_channels[ch_pos])
        self._ch_neg = AnalogIn(self._mcp, mcp_channels[ch_neg])
        self._ch_gnd = AnalogIn(self._mcp, mcp_channels[ch_gnd])

    def obtain_sample(self):
        """Return channel data with ECG signal value obtained from samples at given time."""
        # Note channel.value is a 16-bit integer, but the MCP is a 10-bit ADC.
        LL = self._ch_pos.value
        LA = self._ch_neg.value
        RA = self._ch_gnd.value
        ecg = RA - 0.5 * (LA + LL)

        return LL, LA, RA, ecg
