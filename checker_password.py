import string
import random

length = 10

characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(length))

print("Generated Password:", password)



