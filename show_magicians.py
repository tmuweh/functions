
def show_magicians(modified_magicians):

	for name in modified_magicians:

		print(name)

def make_great(magicians, modified_magicians):

	for name in magicians:
		modified_magicians.append("the Great " + name.title())

magicians = ['tangue', 'aburo', 'agbor', 'dona']
modified_magicians = []
make_great(magicians[:], modified_magicians)
show_magicians(modified_magicians)

