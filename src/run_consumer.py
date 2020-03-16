from streaming.consumer import Consumer
from visualization.printer import Printer
from visualization.plotter import Plotter


def run_with_printer():
    consumer = Consumer()
    printer = Printer('TIME', 'ECG')

    printer.print_headers()

    while True:
        samples, timestamp = consumer.pull_data()
        printer.display_data(timestamp, *samples)


def run_with_plotter():
    consumer = Consumer()
    plotter = Plotter(1)
    plotter.display_data(lambda: consumer.pull_data()[0])


if __name__ == '__main__':
    run_with_plotter()
