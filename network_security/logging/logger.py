import logging, os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%S')}.log"

log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)