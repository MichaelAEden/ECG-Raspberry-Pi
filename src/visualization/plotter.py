#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plotter:

    # Number of data points to record before plotting.
    _BUFFER_SIZE = 25

    # Maximum number of data points to graph at any given point.
    _DATA_POINTS_MAX = 100

    def __init__(self, channel_count):
        self._channel_count = channel_count
        self._channels = np.zeros(channel_count)

    def display_data(self, sample_period_ms, sample_data):
        """
        Plots data using Matplotlib. Note this function will run indefinitely, so we pass in a
        function get sample data and the rate at which to sample.

        :param sample_period_ms: Sampling period in milliseconds.
        :param sample_data: Function for getting sample data.
        """
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        def animate(_):
            ax.clear()
            for i in range(self._BUFFER_SIZE):
                self._channels = np.vstack((self._channels, sample_channels()))

            # Trim data to keep under maximum number of data points.
            if channels.shape[0] > self._DATA_POINTS_MAX:
                channels = channels[(channels.shape[0] - self._DATA_POINTS_MAX):, :]

            # Plot each channel.
            for channel in channels.T:
                ax.plot(channel)

        ani = animation.FuncAnimation(fig, animate, interval=sample_period_ms)
        plt.show()
