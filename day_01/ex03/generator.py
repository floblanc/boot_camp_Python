# import string
from random import shuffle

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if (option != "ordered" and option != "shuffle" and option != "unique" and option != "") or not isinstance(text, str):
		print("ERROR")
		exit()
	li = text.split(sep)
	if option == "ordered":
		li.sort()
	elif option == "shuffle":
		shuffle(li)
	elif option == "unique":
		sorted(set(li))
	for x in li: 
		yield x
