import time


def print_headers(channel_count):
	channels = []
	for i in range(channel_count):
		channels.append("CH" + str(i))

	row_format ="{:>15}" * (len(channels))
	print(row_format.format(*channels))


def print_data(data):
	row_format ="{:>15}" * (len(data))
	print(row_format.format(*data))


if __name__ == '__main__':
	CHANNELS = 8

	print_headers(CHANNELS)

	while True:
		print_data([1, 2, 5, 6, 1, 2, 3, 4])
		time.sleep(1)
