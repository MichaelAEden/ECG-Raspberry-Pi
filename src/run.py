#!/usr/bin/python3

import time

from streaming.streamer import Streamer
from visualization.printer import Printer
from visualization.plotter import Plotter
from ecgcollection.ecg_collector import EcgCollector


# Constants
CHANNEL_COUNT = 8
SAMPLE_PERIOD = 0.0025
SAMPLE_FREQ_HZ = int(1.0 / SAMPLE_PERIOD)

CH_POSITIVE = 5
CH_NEGATIVE = 6
CH_GROUND = 7


def run_with_printer():
        ecg_collector = EcgCollector(
                ch_pos = CH_POSITIVE,
                ch_neg = CH_NEGATIVE,
                ch_gnd = CH_GROUND
        )
        streamer = Streamer(1, SAMPLE_FREQ_HZ)
        printer = Printer('POS', 'NEG', 'GND', 'ECG')

        sample_count = 0
        run_time = time.time()
        while True:
                start = time.time()

                positve, negative, ground, ecg_data = ecg_collector.obtain_sample()
                #printer.display_data(positve, negative, ground, ecg_data)
                #streamer.stream_data(ecg_data)

                ## This seems to be more accurate than sleep.time.
                #while (time.time() - start) < SAMPLE_PERIOD:
                #        pass

                sample_count += 1

                if sample_count % SAMPLE_FREQ_HZ == 0:
                        print('Obtained {} samples over {} seconds'.format(sample_count, time.time() - run_time))
                        break


if __name__ == '__main__':
        run_with_printer()
