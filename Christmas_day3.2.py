#!/usr/bin/env python3
import string
from itertools import islice

def letterkey(l) :
	letterslist = list(string.ascii_lowercase + string.ascii_uppercase)
	keydict = dict()
	for k in range(0, 52) :
		keydict[letterslist[k]] = k + 1
	return keydict[l]

with open(r"input3.txt", 'r') as fp :
	for count, line in enumerate(fp) :
		pass
print('Total Lines', count + 1)

bagelist = list()
with open("input3.txt", 'r') as newfile:
	lines = list()
	for line in newfile:
		line = line.rstrip()
		lines.append(line)
		if len(lines) >= 3:
			print(lines)
			print("STOP")
			a = list(lines[0])
			b = list(lines[1])
			c = list(lines[2])
			for letter in a :
				if (letter in b) and (letter in c) :
					print("Same letter!", letter)
					sameletter = letter
					bagelist.append(sameletter)
					break
			print(a)
			lines = list()
	if len(lines) > 0 :
		print(lines)
print(len(bagelist))
print(bagelist)
#for line in lines_gen:
#    print(line)



#print(letterkey("l"))
sumb = 0
for m in bagelist :
	sumb = sumb + int(letterkey(m))

print("total sum", sumb)
