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
1. Download the zip file, and extract it. The scripts should be in `Ransomware-Script-main` folder.
2. (optional) Add aditional files which you would like to encrypt into the `Ransomware-Script-main` folder.
3. Try to open `Test_Pdf_file.py` and `test_file.txt` to see if data is present.
4. Encrypt all the files within the folder (except `encrypt.py`, `decrypt.py` and `key_file.key` (which will be generated during the encryption process)). Use the following command in the present-working-directory:-

```python
python encrypt.py
```
4. Try to open the encrypted files `Test_Pdf_file.py` and `test_file.txt` and view their content.
5. Decrypt the files using using the command:-
```python
python decrypt.py
```
PLEASE NOTE: The script will ask for a password before decrypting the file. The password is: `ransome`. (Check the below given example)

6. Try to view the files again. This time, they should be decrypted back.

## **Example**
Here, we can see all the files from the zip file.

![image](https://user-images.githubusercontent.com/61109976/169681749-db8c46e6-bdb1-428c-9fad-0ff7fc226ee4.png)


And here, we can see the files with their content without encryption.'

![image](https://user-images.githubusercontent.com/61109976/169681808-e36fb14b-e599-4b90-89b0-b5b4766abab3.png)


Now, we encrypt the files.

![image](https://user-images.githubusercontent.com/61109976/169681841-af276f5d-7f2e-4a5d-b53a-9c18786074c2.png)


Here, we can see, the data is encrypted, hence the following output.

![image](https://user-images.githubusercontent.com/61109976/169681864-0b046c7b-577d-4209-9e16-9b9639d3163b.png)


Now, we decrypt the files.

![image](https://user-images.githubusercontent.com/61109976/169681892-be6b20ab-35bb-44f9-9d29-869a3040352e.png)

And here, we have recovered the files back after the decryption process.
![image](https://user-images.githubusercontent.com/61109976/169681922-a0278f17-2bc8-460a-904c-10ba0dd2f8cc.png)
