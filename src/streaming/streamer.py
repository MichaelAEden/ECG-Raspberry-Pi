#!/usr/bin/python3

# Based on: https://github.com/labstreaminglayer/liblsl-Python/blob/master/pylsl/examples/SendData.py

import time
import uuid
from pylsl import StreamInfo, StreamOutlet


class Streamer:

    def __init__(self, channels, sample_rate):
        self._channels = channels

        # Create a StreamInfo object with stream metadata.
        # ECG is not listed under accepted types (see https://github.com/sccn/xdf/wiki/Meta-Data),
        # so we'll use EEG as a placeholder.
        stream_info = StreamInfo(
            'RaspPiECG',
            'EEG',
            channels,
            sample_rate,
            'float32',
            'raspberrypi-' + str(uuid.uuid4())
        )

        # Create an outlet; this will be used to stream data.
        self._stream_outlet = StreamOutlet(stream_info)

    def stream_data(self, *data):
        if len(data) != self._channels:
            print('[Streamer] WARNING: Number of samples does not match number of channels.')
            return
    
        self._stream_outlet.push_sample(data)
