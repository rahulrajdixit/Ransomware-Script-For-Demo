# Ransomware-Script

## **Please Note**

> [!WARNING] 
> Please consider running these scripts only if you can clearly understand the working of the script. It is adviced to go through the code before running it. If you like to tinker with these scripts, then please consider running these scripts in a safe environment (Example: in a virtual machine).

> [!IMPORTANT]
> These are python scripts just to demonstrate the working process of a simple ransomware. Actual ransomwares have a much more complex working process, are not as simple as these scripts.

> [!NOTE]
> The tool can only encrypt and decrypt files (and not folders) within the same directory of the python scripts.
> This project was developed out of curiosity with the help of some references. Please do not misuse the script and use it only for educational/demonstration purpose.

## **Introduction**
These python scripts encrypt and decrypt the files within the same directory using Fernet Encryption.

The folder consists of 2 scripts:
- `encrypt.py`: For encrypting all the files using Fernet Encryption
- `decrypt.py`: For decrypting all the files.

A separate file named "key_file.key" is generated during the encryption process, and the key present within this file is used duirng the decryption process. Please note that the generated key is unique every time "encrypt.py" secript is run, and the key within "key_file.key" is replaced every time.

A password is required during the decryption process, which is asked by the script. The current password to decrypt the files is `ransome` (Check line 37 of `decrypt.py` file for a better understanding).

-----------------------------------------------------

## **How to use it?**
1. Download the zip file, and extract it. The scripts should be in the `Ransomware-Script-main` folder.
2. (optional) Add aditional files which you would like to encrypt into the `Ransomware-Script-main` folder.
3. Try to open `Test_PDF_File.py` and `test_file.txt` to see if data is present.
4. Encrypt all the files within the folder (except `encrypt.py`, `decrypt.py` and `key_file.key` (which will be generated during the encryption process)). Use the following command in the present-working-directory:-

```python
python encrypt.py
```
4. Try to open the encrypted files `Test_PDF_File.py` and `test_file.txt` and view their content.
5. Decrypt the files using using the command:-
```python
python decrypt.py
```
PLEASE NOTE: The script will ask for a password before decrypting the file. The password is: `ransome`. (Check the below given example)

6. Try to view the files again. This time, they should be decrypted back.

## **Example**
Here, we can see all the files from the zip file.

![image](https://user-images.githubusercontent.com/61109976/169683167-0904c437-2c6a-4900-92d0-ce27f416b457.png)


And here, we can see the files with their content without encryption.

![image](https://user-images.githubusercontent.com/61109976/169681808-e36fb14b-e599-4b90-89b0-b5b4766abab3.png)


Now, we encrypt the files.

![image](https://user-images.githubusercontent.com/61109976/169681841-af276f5d-7f2e-4a5d-b53a-9c18786074c2.png)


Here, we can see, the data is encrypted, hence the following output.

![image](https://user-images.githubusercontent.com/61109976/169681864-0b046c7b-577d-4209-9e16-9b9639d3163b.png)


Now, we decrypt the files.

![image](https://user-images.githubusercontent.com/61109976/169681892-be6b20ab-35bb-44f9-9d29-869a3040352e.png)

And here, we have recovered the files back after the decryption process.

![image](https://user-images.githubusercontent.com/61109976/169681922-a0278f17-2bc8-460a-904c-10ba0dd2f8cc.png)
