#logging in a function
import logging
logging.basicConfig(filename="result.log",
                    level=logging.DEBUG,
                 format="%(asctime)s-%(levelname)s-%(message)s")
 
def add(a,b):
    logging.info("Entered add() function")
    logging.debug(f"Input values: a={a}, b={b}")
    
    result = a + b
    
    logging.info(f"Addition result: {result}")
    return result
def divide(a,b):
    logging.info("Entered divide() function")
    logging.debug(f"Input values: a={a}, b={b}")
    
    if b == 0:
        logging.error("Division by zero attempted")
        raise ZeroDivisionError("Cannot divide by zero")
    
    result = a / b
    logging.info(f"Division result: {result}")
    return result
try:
    logging.info("Program started,taking user input")
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    add_result = add(a, b)
    divide_result = divide(a, b)
except ValueError:
    logging.critical("Input Invalid")
except Exception as e:
    logging.critical(f"Unexpected error occurred: {e}")

finally:
    logging.info("Program ended")
