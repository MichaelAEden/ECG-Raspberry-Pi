#!/usr/bin/python3


class Printer:

    def __init__(self, *headers):
        self._channel_count = len(headers)

        self._print_headers(headers)

    def _print_headers(self, headers):
        header_format = '{:>15}' * self._channel_count
        print(header_format.format(*headers))

    def display_data(self, *data):
        if len(data) != self._channel_count:
            print('[Printer] WARNING: Number of samples does not match number of channels.')
            return

        _row_format = '{:>15.3f}' * self._channel_count
        print(_row_format.format(*data))
