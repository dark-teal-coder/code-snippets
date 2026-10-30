import secrets 
import string 


alpha_num = string.ascii_letters + string.digits
password = "".join(secrets.choice(alpha_num) for _ in range(6))
print("Generated password:", password)
