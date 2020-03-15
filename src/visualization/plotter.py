#!/usr/bin/python3

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plotter:

    # Number of data points to record before plotting.
    _BUFFER_SIZE = 50

    # Maximum number of data points to graph at any given point.
    _DATA_POINTS_MAX = 200

    def __init__(self, channel_count, sample_period):
        self._channel_count = channel_count
        self._channels = np.zeros(channel_count)
        self._sample_period = sample_period
        self._sample_freq = int(1 / sample_period)

    def display_data(self, sample_data):
        """
        Plots data using Matplotlib. Note this function will run indefinitely, so we pass in a
        function get sample data and the rate at which to sample.

        :param sample_data: Function for getting sample data.
        """
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        self._sample_count = 0
        self._start_time = time.time()

        def animate(_):
            ax.clear()

            # Collect a few samples before displaying.
            for i in range(self._BUFFER_SIZE):
                start = time.time()
                self._channels = np.vstack((self._channels, np.asarray(sample_data())))

                self._sample_count += 1

                # More accurate than time.sleep()
                while (time.time() - start) < self._sample_period:
                    pass

                if self._sample_count % self._sample_freq == 0:
                    print('Obtained {} samples over {} seconds'.format(self._sample_count, time.time() - self._start_time))

            # Trim data to keep under maximum number of data points.
            if self._channels.shape[0] > self._DATA_POINTS_MAX:
                self._channels = self._channels[(self._channels.shape[0] - self._DATA_POINTS_MAX):, :]

            # Plot each channel.
            for channel in self._channels.T:
                ax.plot(channel)

        ani = animation.FuncAnimation(fig, animate, interval=1)
        plt.show()
