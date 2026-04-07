#Online order processing system

import logging

logger=logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

#info handler
info_handler=logging.FileHandler("activity1.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

#error handler
error_handler=logging.FileHandler("error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)

try:
    logger.info("Program started")
    customer_name=input("enter customer name")
    product_price=int(input("enter your product  price "))
    quantity=int(input("enter quantity you want"))

    logger.info("user input received")
    if product_price<=0:
        logger.error("Price should be non negative,check once again")
        raise ValueError("Invalid price")
    if quantity < 0:
        logger.warning("quantity should be positive")
        raise ValueError("Invalid quantity")

    total= product_price * quantity

    logger.info(f"total calculated,Total= {total}")

    if total>10000:
        logger.warning("High value order detected")
except ValueError as ve:
    logger.error(f"Input validation error: {ve}")
except Exception as e:
    logger.exception(f"Unexpected exception occured")

finally:
    logger.info("program completed")