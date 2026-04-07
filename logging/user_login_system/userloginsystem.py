import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s")
logging.info("program started")
found=False
try:
    username=input("enter username")
    password=input("enter password to login")
    logging.info(f"logging attempt for username:{username}")
    with open("users.txt","r") as f:
        logging.debug("User database file opened successfully")
        for line in f:
            line=line.strip()
            stored_username,stored_password=line.split(",")
            if username==stored_username and password==stored_password:
                found=True
                break
    if found:
        logging.info(f"User {username} logged in successfully")
    else:
        logging.warning(f"Failed login attempt for username:{username} or check the username once again")
except FileNotFoundError:
    logging.error("Error accessing user database file.")
