# Ransomware-Script

## **Please Note**
- Please consider runnng these scripts only if you can clearly understand the working of the script . It is adviced to go through the code before running it. Consider running these scripts in a save environment (Example: in a virtual machine) if you would like to tinker with these scripts.
- Please note, this is just a simple python script to show how ransomwares work.
- The tool can only encrypt and decript files within the same directory of the python scripts.
- Actual ransomwares have a much more complex working process, are not as simple as this script.
- This project was developed made out of curiosity with the help of some resources. Please do not misuse the script and use it only for educational purpose.

## **Introduction**
These python scripts encrypt and decrypt the files within the same directory using Fernet Encryption.

The file consists of 2 scripts: 
- `encrypt.py`: For encrypting all the files using Fernet Encryption
- `decrypt.py`: For decrypting all the files.

A separate file named "key_file.key" is generated during the encryption process, and the key present within this file is used duirng the decryption process. Please note that the generated key is unique every time "encrypt.py" secript is run, and the key within "key_file.key" is replaced every time.

-----------------------------------------------------

## **How to use it?**
1. Download the zip file, and extract it. The scripts should be in `Ransomware-Script` folder.
2. Add aditional files you would like to encrypt into the `Ransomware-Script` folder.
3. Run encryption for all the files within the folder (except `encrypt.py`, `decrypt.py` and `key_file.key` (which will be generated during the encryption process). Use the following command in the present-working-directory:-

```python
python3 encrypt.py
```
4. Try to open the encrypted files and view their content.
5. Decrypt the files using using the command:-
```python
python3 decrypt.py
```
6. Try to view the files again. This time, they should be decrypted back.
