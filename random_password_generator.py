import secrets 
import string 


def generate_password(digit):
    alpha_num = string.ascii_letters + string.digits
    ## Randomly choose a letter or number for N times where N = number of digits. 
    password = "".join(secrets.choice(alpha_num) for _ in range(digit))
    return password


## Specify the number of digits for parameter "digit".
password = generate_password(6)
print("Generated password:", password)
