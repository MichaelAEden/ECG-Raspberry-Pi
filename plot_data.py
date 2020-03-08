import time
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# Amount of data to cache before plotting.
BUFFER_SIZE = 25

# Maximum number of data points to graph at any given point.
TIME_SERIES_POINTS_MAX = 100

# Sample period in seconds.
SAMPLE_PERIOD = 0.01


CHANNEL_COUNT = 5


channels = np.zeros(CHANNEL_COUNT)


def plot_voltages():
    """channel_data is a 2D array"""
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def animate(_):
        global channels

        ax.clear()
        for i in range(BUFFER_SIZE):
            channels = np.vstack((channels, sample_channels()))
            time.sleep(SAMPLE_PERIOD)

        if channels.shape[0] > TIME_SERIES_POINTS_MAX:
            channels = channels[(channels.shape[0] - TIME_SERIES_POINTS_MAX):, :]

        for voltages in channels.T:
            ax.plot(voltages)

    ani = animation.FuncAnimation(fig, animate, interval=1)
    plt.show()


def sample_channels():
    return np.random.random(CHANNEL_COUNT)


def run():
    plot_voltages()


if __name__ == '__main__':
    run()
