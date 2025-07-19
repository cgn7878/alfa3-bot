# log.py

import logging
from datetime import datetime

def log_kur():
    """
    Log sistemini kurar.
    """
    zaman = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dosyası = f"logs/log_{zaman}.log"

    logging.basicConfig(
        filename=log_dosyası,
        filemode='a',
        format='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
