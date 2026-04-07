import logging
#logging to file
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)    #capture all levels
# create file handler
file_handler=logging.FileHandler("activity.log",mode="a")   #append mode
file_handler.setLevel(logging.DEBUG)   #show all messages in file
#create formatter
formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)    #add handler to logger
# log messages of different levels
logger.debug("Debugging program started")
logger.info("User logged in")
logger.warning("Password will expire soon")
logger.error("Failed to load user profile")
logger.critical("Database connection lost ")

print("All logs are saved to 'activity.log' file")

