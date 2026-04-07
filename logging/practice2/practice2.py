#logging to a file

import logging

logging.basicConfig(filename="app.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s=%(message)s")

logging.info("log file created")

for i in range(1,6):
    logging.debug(f"Loop iteration number: {i}")

logging.info("program ended successfully")