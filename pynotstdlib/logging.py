import logging
import sys


def default_logging(logging_level: int = logging.INFO):
    root = logging.getLogger()
    root.setLevel(logging_level)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]')
    ch.setFormatter(formatter)
    root.addHandler(ch)
