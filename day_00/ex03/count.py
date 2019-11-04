import string

def text_analyzer(src = 0):
	"""This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
	upper = 0
	lower = 0
	punct = 0
	spaces = 0
	if src == 0:
		src = input("What is the text to analyse?\n>> ")
	for c in src:
		if c.isupper():
			upper += 1
		elif c.islower():
			lower +=1
		elif c == ' ':
			spaces +=1
		elif c in string.punctuation:
			punct +=1
	print("The text contains " + str(len(src)) + " characters:")
	if upper > 0:
		print("- " + str(upper) + " upper letters")
	if lower > 0:
		print("- " + str(lower) + " lower letters")
	if punct > 0:
		print("- " + str(punct) + " punctuation marks")
	if spaces > 0:
		print("- " + str(spaces) + " spaces")