import logging
import os
from datetime import datetime

LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

log_path = os.path.join(os.getcwd(), 'logs')

os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO,
                    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')