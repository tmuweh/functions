
def show_magicians(magicians, modified_magicians):

	print(magicians)
	print(modified_magicians)

def make_great(magicians, modified_magicians):

	for name in magicians:
		modified_magicians.append("the Great " + name.title())

	return modified_magicians

magicians = ['tangue', 'aburo', 'agbor', 'dona']
modified_magicians = []
make_great(magicians[:], modified_magicians)
show_magicians(magicians, modified_magicians)

