# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import secrets
import hashlib

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def gen_hash():
    # Generate a random string of a specified length (e.g., 16 bytes)
    random_data = secrets.token_bytes(16)
    # Create a hash of the random data (using SHA-256 in this example)
    hash_key = hashlib.sha256(random_data).hexdigest()
    print('Random Hash Key:', hash_key)


gen_hash()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    gen_hash()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
