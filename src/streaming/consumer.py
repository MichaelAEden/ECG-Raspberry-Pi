#!/usr/bin/python3

# Based on
# https://github.com/neurotechuoft/Neurostack/blob/cd2f8f460ccb40c3bb7f9d30f33ad92ea6e3658f/neurostack/data_streams/data_stream.py
# https://github.com/labstreaminglayer/liblsl-Python/blob/master/pylsl/examples/ReceiveData.py

from pylsl import StreamInlet, resolve_byprop


class Consumer:

    def __init__(self):
        streams = resolve_byprop('type', 'EEG', timeout=30)
        if len(streams) == 0:
            raise RuntimeError('Could not find EEG stream')
        elif len(streams) > 1:
            raise RuntimeError('Found multiple EEG streams')
        self._inlet = StreamInlet(streams[0])

    def pull_data(self):
        samples, timestamp = self._inlet.pull_sample()
        time_correction = self._inlet.time_correction()

        return (samples, timestamp)
