import logging

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, force=True)


def get_logger(name):
    return logging.getLogger(name)
