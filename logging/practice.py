import logging

#basic log messages

#configure logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

logging.info("Program Started")

#sample calculation
a=10
b=5
logging.debug(f"values before calculation: a={a} ,b={b}")

result=a+b

logging.debug(f"calculation performed:{a} + {b}")
logging.info(f"Result:{result}")


#log different levels
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(levelname)s-%(message)s' )
try:
    logging.info("program Started .Taking input from user")
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    logging.debug(f"values before calculation are a={a} and b={b}")
    logging.info("checking conditions....")
    if a<0 or b<0:
        logging.warning("one or both numberes are negative")
    if b==0:
        logging.error("Division by  0 not allowed")
    else:
        res=a/b
        logging.info("Division success.Result= ",res)
except ValueError:
    logging.critical("Input Invalid")
except Exception as e:
    logging.critical(f"Unexpected error occurred: {e}")

finally:
    logging.info("Program ended.")






