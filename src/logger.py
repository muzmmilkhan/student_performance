import logging
import os
import sys
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
LOG_DIR = os.makedirs('logs',exist_ok=True)
LOG_FILE_PATH = os.path.join(os.getcwd(),'logs',LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] - %(lineno)s %(name)s - %(message)s',
    level= logging.INFO
)

def get_logger(name):
    return logging.getLogger(name=name)