# Execute with python3 hashcalc.py
#import module
import crypt

while True:
	print ("I am an encryption script.\nI encrypt a series of characters")
	print ("and numbers in 5 algorithms!!!")
	print ("System Running...\n")
	print ("opprssr wrote it....")
	print ("                  x 0")
	print ("                 ~~~~~\n")

	encrypts = [
		'md5',
		'blowfish',
		'sha256',
		'crypt',
		'hex',

	]

	for encrypt in encrypts:
		print ("\t* " + encrypt + "\n")

	print ("Enter 'md5' for MD5 algorithm.")
	print ("Enter 'blowfish' for blowfish algorithm.")
	print ("Enter 'sha256' for sha256 algorithm.")
	print ("Enter 'crypt' for crypt algorithm.")
	print ("Enter 'hex' for hex algorithm.")
	print ("Enter 'exit' to exit the program.")

	encrypt = input("Enter an encryption choice from above: > ")

	if encrypt == 'exit':
		break

	elif encrypt == 'md5':
		enc = input("input here: > ")
		print ("[*] Your md5 hash is: >", crypt.crypt(enc, "MD5"))
		print ("\n")

	elif encrypt == 'blowfish':
		enc = input("input here: > ")
		print ("[*] Your blowfish hash is: >", crypt.crypt(enc, "BLOWFISH"))
		print ("\n")
	elif encrypt == 'sha256':
		enc = input("input here: >")
		print ("[*] Your SHA256 bit hash is: >", crypt.crypt(enc, "SHA256"))
		print ("\n")

	elif encrypt == 'crypt':
		enc = input("input here: > ")
		print ("[*] Your crypt hash is: >", crypt.crypt(enc, "CRYPT"))
		print ("\n")

	elif encrypt == 'hex':
		enc = input("input here: > ")
		print ("[*] Your Hex hash is: >", crypt.crypt(enc, "HX"))
		print ("\n")

	else:
		print ("Encryption Failure...")
