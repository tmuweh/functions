
#list to store numbers
l = []

#divisible by 7 but not divisible by 5
for i in range(2000, 3201):
	if(i%7 == 0 and i%5!= 0):
		l.append(str(i))

#print words comma separated
print(','.join(l))