import os
import random

print('------------------------\n-  eezCrypt Algorythm  -\n------------------------')

seed = 0
fileToEncrypt = input ('Name of the file to encrypt : ')
mode = 'r'

# ------------------------------------

def generateKey(bits):
	key = ''
	chars = '0123456789abcdef'
	seed = int(bits / 8 * 7)
	for i in range(bits):
		index = random.randint(0,len(chars)-1)
		key += chars[index]

	set = (key, seed)

	return set

# ----------------------------------------------------------------------------------------

def getValues(string):
	values = [0] * len(string)
	for i in range(len(string)):
		if(string[i]=='a'):
			values[i] = '10'
		elif(string[i]=='b'):
			values[i] = '11'
		elif(string[i]=='c'):
			values[i] = '12'
		elif(string[i]=='d'):
			values[i] = '13'
		elif(string[i]=='e'):
			values[i] = '14'
		elif(string[i]=='f'):
			values[i] = '15'
		else:
			values[i] = string[i]

	return values
	
# ----------------------------------------------------------------------------------------

def compareValues(len_values, j):
	if(j>=len_values-1):
		j -= len_values
		if(j>=len_values):
			compareValues(len_values, j)
	return j
	
# ----------------------------------------------------------------------------------------

print('\n\nRepo : ' + os.getcwd())

if os.path.exists(fileToEncrypt):
	encryptOrNot = input('Would you like to encrypt or to decrypt this file (e/d)?')

	if encryptOrNot == 'e':
		with open(fileToEncrypt, mode) as file :
			bin = file.read().encode('utf-8').hex()
			print('\n\n')
			# print(bin)
	
		datas = generateKey(256)
			
		unc_values = getValues(bin)
		for i in range(len(unc_values)):
			print(unc_values[i])
		key_values = getValues(datas[0])
	
		result_values = [0] * (len(unc_values)+1)
			
		for i in range(len(unc_values)):
			j = i
			while j >= len(key_values):
				j -= len(key_values)
			result_values[i] = str(
	int(unc_values[i]) + int(key_values[j]))
			print(result_values[i])
			result_lengths = [0] * len(result_values)
			for i in range(len(result_values)):
				result_lengths[i] = len(str(result_values[i]))
				print(result_lengths[i])

# ----------------------------------------------------

		mode = 'w'
		with open(fileToEncrypt, mode) as file:
			for i in range(len(result_values)):
				file.write(str(result_values[i]))
	
		with open('key.txt', 'x') as file:
			file.write(datas[0])

	elif encryptOrNot == 'd':
		# Here

		else:
			print('Invalid value')
			
else: print("This file doesn't exist")
