#!/usr/bin/python3

from app import app

import os
import logging
from logging.handlers import RotatingFileHandler

version = '0.0.1'


def initialize_logger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = RotatingFileHandler(filename=os.path.join(output_dir, "app.log"), mode='w', maxBytes=1*1024*1024, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.info('version: {}'.format(version))


initialize_logger(os.path.dirname(os.path.realpath(__file__)))
app.run(host='0.0.0.0', port=5055)
