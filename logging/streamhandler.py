# simple logging

import logging
#creating logger
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)    #capture all levels

console_handler=logging.StreamHandler()   # create console handler
console_handler.setLevel(logging.DEBUG)   #show all messages in console
#create formatter
formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)    #add handler to logger
# log messages of different levels
logger.debug("Debugging program started")
logger.info("User logged in")
logger.warning("Password will expire soon")
logger.error("Failed to load user profile")
logger.critical("Database connection lost ") 



