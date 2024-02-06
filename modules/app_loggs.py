# Import the logging and sys modules
import logging
import sys
# Import the TimedRotatingFileHandler class from the logging.handlers module
from logging.handlers import TimedRotatingFileHandler
# Define a formatter for the log messages
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
# Define a file name for the log file
LOG_FILE = "my_app_logs.log"

# Define a function to create a console handler for the logger
def get_console_handler():
  # Create a StreamHandler object that writes to the standard output
  console_handler = logging.StreamHandler(sys.stdout)
  # Set the formatter for the console handler
  console_handler.setFormatter(FORMATTER)
  # Return the console handler
  return console_handler

# Define a function to create a file handler for the logger
def get_file_handler():
  # Create a TimedRotatingFileHandler object that rotates the log file at midnight
  file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
  # Set the formatter for the file handler
  file_handler.setFormatter(FORMATTER)
  # Return the file handler
  return file_handler

# Define a function to create and configure a logger object
def get_logger(logger_name):
  # Get a logger object with the given name
  logger = logging.getLogger(logger_name)
  # Set the logging level to DEBUG to capture all the logs
  logger.setLevel(logging.DEBUG)
  # Add the console handler and the file handler to the logger
  logger.addHandler(get_console_handler())
  logger.addHandler(get_file_handler())
  # Disable the propagation of the logs to the parent logger
  logger.propagate = False
  # Return the logger object
  return logger

