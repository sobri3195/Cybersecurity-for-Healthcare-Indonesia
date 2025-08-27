import logging
from config.settings import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(msg):
    print(f"[INFO] {msg}")
    logging.info(msg)

def log_warning(msg):
    print(f"[WARNING] {msg}")
    logging.warning(msg)

def log_alert(msg):
    print(f"[ALERT] {msg}")
    logging.critical(msg)
