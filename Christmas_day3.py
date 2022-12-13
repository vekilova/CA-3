#!/usr/bin/env python3


import string

def letterkey(l) :
	letterslist = list(string.ascii_lowercase + string.ascii_uppercase)
	keydict = dict()
	for k in range(0, 52) :
		keydict[letterslist[k]] = k + 1
	return keydict[l]

hfile = open('input3.txt')
#newline = 'NJvhJcQWTJWTNTFFMTqqGqfTmB'

errorlist = list()

for line in hfile :
	print("############NEWLINE#############")
	line = line.rstrip()
	print(line)
	linelist = list(line)

#	print(linelist)
	print(len(linelist))
	half = int(len(linelist)/2)
	tot = int(len(linelist))
	print(half, tot)


	break_out_flag = False
	for i in range(0, half) :
#		print('i=', linelist[i])
		for j in range(half, tot) :
#			print('j=', linelist[j], end = " ")
			if linelist[i] == linelist[j] :
				break_out_flag = True
				let = linelist[i]
				break
		if  break_out_flag :
			break
	errorlist.append(let)

print(errorlist)


#print(letterkey("l"))
sume = 0
for m in errorlist :
	sume = sume + int(letterkey(m))

print("total sum", sume)
