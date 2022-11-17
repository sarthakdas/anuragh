from cryptography.fernet import Fernet 
import time
# kind is what will be encrypted. So if you put "psw" the password will be encrypted and if you put "usr" the username will be encrypted. If you don't want it then don't use it.



def encrypt(psw, kind):
	if kind == "psw":
		with open('key.bin', 'rb') as key_file:
			key_read = key_file.read()
			f = Fernet(key_read)
			encrypted = f.encrypt(psw.encode())
			key_file.close()
			with open('password.bin', 'ab') as pwd_list:
				pwd_list.write(encrypted+"\n".encode())
				pwd_list.close()
	elif kind == "usr":
		with open('key.bin', 'rb') as key_file:
			key_read = key_file.read()
			f = Fernet(key_read)
			encrypted = f.encrypt(psw.encode())
			key_file.close()
			with open("username.bin", 'rb') as usr_list:
				usrs = usr_list.readlines()
				for line in usrs:
					decrypted = f.decrypt(line)
					if psw.encode() in decrypted:
						print("Error: This username has already been taken!")
						return False
			with open('username.bin', 'ab') as usr_list:
				usr_list.write(encrypted+"\n".encode())
				usr_list.close()
				return True
	else:
		raise TypeError
		return False


# All this function does is decrypt all the passwords/usernames and makes and checks to see if the password/username is the same. Nothing is ever stored or can be called without changing code. And even then if you are using this it's supposed to be encrypted and on a server!
usr_line = 0
def decrypt(psw, kind):
	global usr_line
	if kind == "psw":
		with open('key.bin', 'rb') as key_file:
			key_read = key_file.read()
			f = Fernet(key_read)
			with open('password.bin','rb') as pwd_list:
				pwds = pwd_list.readlines()
				for i, line in enumerate(pwds):
					if i == usr_line:
						if psw.encode() in f.decrypt(line):
							return True
			return False
	elif kind == "usr":
		with open('key.bin', 'rb') as key_file:
			key_read = key_file.read()
			f = Fernet(key_read)
			with open('username.bin','rb') as usr_list:
				usrs = usr_list.readlines()
				for i, line in enumerate(usrs):
					usr_line = i
					if psw.encode() in f.decrypt(line):
						return True
			return False
	else:
		raise TypeError
		return False

def gen_key():
	key = Fernet.generate_key()
	usr = input("Warning: You are about to remove all usernames and passwords and regenerate a new key! Are you sure you want to continue y/n?") 
	if usr.lower() == "y":
		with open('key.bin', 'wb') as f:
			f.write(key)
		with open('password.bin', 'w') as f:
			f.write("")
		with open('username.bin', 'w') as f:
			f.write("")	
		print("Key has been generated and usernames and passwords have been removed. ")
	elif usr.lower() == "n":
		print("Generation aborted")
		time.sleep(3)

		


