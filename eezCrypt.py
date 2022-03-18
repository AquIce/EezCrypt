import os
import random

print('------------------------\n-  eezCrypt Algorythm  -\n------------------------')

BITS = 256
seed = 0
fileToEncrypt = input ('Name of the file to encrypt : ')
mode = 'r'

# ------------------------------------

def generateKey(bits):
	key = ''
	chars = '0123456789abcdef'
	for i in range(bits - 4):
		index = random.randint(0,len(chars)-1)
		key += chars[index]

	return key

# ----------------------------------------------------------------------------------------

def getValues(string):
	values = [0] * len(string)
	for i in range(len(string)):
		if(string[i]=='a'):
			values[i] = 10
		elif(string[i]=='b'):
			values[i] = 11
		elif(string[i]=='c'):
			values[i] = 12
		elif(string[i]=='d'):
			values[i] = 13
		elif(string[i]=='e'):
			values[i] = 14
		elif(string[i]=='f'):
			values[i] = 15
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

def getPassages():
	return random.randint(0,9)
	
# ----------------------------------------------------------------------------------------

def getAddMode():
	return random.randint(0, 2)
	
# ----------------------------------------------------------------------------------------

def getFrequence():
	return random.randint(1, 3)
	
# ----------------------------------------------------------------------------------------

def getOffset():
	return random.randint(0, 9)

# ----------------------------------------------------------------------------------------

def decimalToBinary(num):
  return bin(num).replace("0b", "")

# ----------------------------------------------------------------------------------------
	
print('\n\nRepo : ' + os.getcwd() + '\n\n')

# Check if the file exists
if os.path.exists(fileToEncrypt):
	# Choose a mode
	encryptOrNot = input('Would you like to encrypt or to decrypt this file (e/d)?')

	# Load the content of the file
	with open(fileToEncrypt, mode) as file :
		content = file.read()
		
	# Convert the content in hexa
	bin = content.encode('utf-8').hex()

	if encryptOrNot == 'e':
		key = generateKey(BITS)
		all = [0] * BITS
		
		for i in range(BITS - 4):
			all[i] = key[i]
			
		all[-4] = getPassages()
		all[-2] = getFrequence()
		
		key = all[:252]
			
		unc_values = getValues(bin)
		for i in range(len(unc_values)):
			print(unc_values[i])
		key_values = getValues(key)
	
		result_values = [0] * (len(unc_values))
		result_lengths = [0] * len(result_values)
		result_offsets = [0] * len(result_values)
		result_add_mode = [0] * len(result_values)
		
		temp = [0] * (len(unc_values))
		for i in range(len(unc_values)):
			temp[i] = int(unc_values[i])

		k = 0
		while k <= all[-4]:
			for i in range(0, len(temp), all[-2]):
				j = i
				while j >= len(key_values):
					j -= len(key_values)
				tempOffset = getOffset()
				tempAddMode = getAddMode()
				
				temp[i] += int(tempOffset)
				
				if tempAddMode == 0: result_values[i] = int(temp[i])
				elif tempAddMode == 1: result_values[i] = int(str(temp[i]) + str(key_values[j]))
				elif tempAddMode == 2: result_values[i] = int(temp[i]) + int(key_values[j])
					
				result_lengths[i] = len(str(result_values[i]))
				result_offsets[i] = tempOffset
				result_add_mode[i] = tempAddMode
				
				temp[i] = result_values[i]
					
			k += all[-2]

		for i in range(len(result_offsets)):
			all[-1] += result_offsets[i]
			all[-3] += result_add_mode[i]

		final = [0] * len(result_values)
		for i in range(len(result_values)): 
			final[i] = decimalToBinary(result_values[i])
		
		mode = 'w'
		with open(fileToEncrypt, mode) as file:
			for i in range(len(result_values)):
				file.write(str(result_values[i]))
	
		with open('key', 'x') as file:
			temp = ''
			for i in range(len(all)):
				temp += str(all[i])
			file.write(temp)

# ----------------------------------------------------

	elif encryptOrNot == 'd':
		print(bin)

	else:
		print('Invalid value')
			
else: print("This file doesn't exist")
