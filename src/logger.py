import logging
import os
from datetime import datetime

# Corrected LOG_FILE format
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"

# Define the log format
LOG_FORMAT = '%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s'

# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO, 
    format=LOG_FORMAT
)

# Create a logger instance
logger = logging.getLogger(__name__)

# if __name__ == '__main__':
#     # Log messages at different levels
#     logger.info('This is an info message')
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')
#     logger.debug('This is a debug message')  # This won't be logged because the level is set to INFO