import os

secret_user = os.getenv('secret_user')
if secret_user:
    print(f"Hello, {secret_user}")
else:
    print("secret_user environment variable is not set.")
