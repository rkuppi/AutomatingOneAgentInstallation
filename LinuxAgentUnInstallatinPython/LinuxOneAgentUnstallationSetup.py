"""
This script will take the inputs from the user and create an encrypted excel file.
During the encryption process key will be generated this is used to decrypt the excel file.
Without this key user cannot open the excel file.
------------------------------------------------------
Inputs:
user is prompted to give the location of actual excel file.
Absolute path is taken as the inputs.
------------------------------------------------------
output:
A file which contain the key is generated and moved to the folder where the script was running.
-------------------------------------------------------
FUTURE SCOPE:
Implementing shared point access to install and place the OneAgent binary in the same folder where the script is placed.
"""
import os
import time
start_time = time.time()
from cryptography.fernet import Fernet
try:
	excelfilelocation = (input(">>Enter full path of Excel file\n"))
	if (os.path.isfile(excelfilelocation)):
		key = Fernet.generate_key()
		with open('unlock.key', 'wb') as unlock:
			unlock.write(key)
		with open(excelfilelocation, 'rb') as original_file:
			original = original_file.read()
		f = Fernet(key)
		encrypted = f.encrypt(original)
		with open ('enc_UnstallationList.xlsx', 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
	else:
    		print("Given path does not exist")
except Exception as E:
	print("Exception", E)

print("Encrypted file is created")
print("Execution  finished in --- %s seconds ---" % (time.time() - start_time))