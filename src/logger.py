import logging
import os
from datetime import datetime

# 1. Create "logs" folder if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# 2. Create a unique log file name using current date & time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 3. Create the full path for the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# 4. Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=='__main__':
    logging.info('logging has started ')