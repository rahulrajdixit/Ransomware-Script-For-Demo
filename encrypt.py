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


# Generate Key

def generate_key_file():
	key = Fernet.generate_key()
	print("Key is:", key)

	with open("key_file.key", "wb") as f:
		f.write(key)
	print("...key-file generated")
	return key


# Encrypt

def encryption_process(files, key):
	print("Encryption started...")

	for file in files:
		with open(file, "rb") as f:
			content = f.read()
		encrypted_content = Fernet(key).encrypt(content)
		with open(file, "wb") as f:
			f.write(encrypted_content)

	print("...encryption complete")


# Main function calls

files = get_file_list()
key = generate_key_file()
encryption_process(files, key)
