import random
import string

# Password length
length = 12

# Available characters
characters = string.ascii_letters + string.digits + "!@#$%^&*"

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

# Display result
print("Generated Password:", password)
