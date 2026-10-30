import secrets 
import string 


alpha_num = string.ascii_letters + string.digits
## Randomly choose a letter or number for 6 times. 
password = "".join(secrets.choice(alpha_num) for _ in range(6))
print("Generated password:", password)
