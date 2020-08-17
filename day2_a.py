import math

def opcodes(lst):
	# get sequences of 4
	# get the item at position 0
	for i in range(math.floor(len(lst)/4)):
		minilst = list_splitter(lst, i*4)
		opcode = minilst[0]
		if (opcode == 1):
			lst[minilst[3]] =  lst[minilst[1]] + lst[minilst[2]]
		elif (opcode == 2):
			lst[minilst[3]] =  lst[minilst[1]] * lst[minilst[2]]
		elif (opcode == 99):
			return lst
		else:
			print('there\'s something wrong with the opcode!')
			return [0]

		if lst[i+4] == 99:
			return lst
	return lst
	# opcode 1:
		# add the item at lst[seq[1]] and lst[seq[2]]
		# set the sum to lst[seq[3]]
	# opcode 2:
		# multiply lst[seq[1]] * lst[seq[2]]
		# set the product to lst[seq[3]]
	# opcode 99:
		# break or return the list

def list_maker(string):
	lst = list(string.split(','))
	for i in range(len(lst)):
		lst[i] = int(lst[i])
	return lst

def list_splitter(lst, ind):
	# get the index by the ind and get the four from there
	newlist = []
	for i in range(ind, ind + 4):
		newlist.append(lst[i])
	return newlist

file = open('input_day2.txt', 'r')
code = list_maker(file.read())
code[1] = 12
code[2] = 2
opped = opcodes(code)
print(opped[0])

file.close()