#calculates factorial of an integer!

def facto(n):
	if n <= 1:
		return 1
	return n * facto(n - 1)