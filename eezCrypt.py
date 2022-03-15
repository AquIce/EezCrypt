import os
import random

seed = 0
fileToEncrypt = 'file.txt'
mode = 'r'

def generateKey(bits):
	key = ''
	chars = '0123456789abcdef'
	seed = int(bits / 8 * 7)
	for i in range(bits):
		index = random.randint(0,len(chars)-1)
		key += chars[index]

	set = (key, seed)

	return set

def cryptKey(set):
	key = set[0]
	seed = set[1]
	return key[:seed]

def getSettings(set):
	key = set[0]
	seed = set[1]
	return key[seed:-4]

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

print('------------------------\n-  eezCrypt Algorythm  -\n------------------------')

print('\n\nRepo : ' + os.getcwd())

if os.path.exists(fileToEncrypt):
	with open(fileToEncrypt, mode) as file :
		bin = file.read().encode('utf-8').hex()
		print('\n\n')
		print(bin)

	datas = generateKey(256)
	print('\n\nCrypt --------------------\n')
	print(cryptKey(datas))
	print('\n\nSettings --------------------\n')
	print(getSettings(datas))
		
	unc_values = getValues(bin)
	key_values = getValues(datas[0])

	result_values = [0] * len(unc_values)
	if(len(unc_values)>len(key_values)):
		for i in range(len(unc_values)):
			j = i
			if(j>=len(key_values)):
				j -= len(key_values)
				if(j>=len(key_values)):
					j -= len(key_values)
					if(j>=len(key_values)):
						j -= len(key_values)
			print('--s')
			print(i)
			print(j)
			print('--e')
			result_values[i] = unc_values[i] + key_values[j]
			print(result_values[i])

	

			
else:
    print("This file doesn't exist")
