username,password=input("enter username and possword to login").split()
found=False
try:
    with open("users.txt","r") as f:
        for line in f:
            line=line.strip()
            stored_username,stored_password=line.split(",")
            if username==stored_username and password==stored_password:
                found=True
                break
    if found:
        print("Login Successful(Found)")
    else:
        print("Login Unsuccessful")
except FileNotFoundError:
    print("User file not found")

