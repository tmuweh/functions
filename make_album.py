
def make_album(artist_name, album_title):
	
	album = {"artist_name": artist_name.title(), "album_title": album_title.title()}
	return album

print(make_album("flavour", "divine"))
print(make_album("semah", "divine"))
print(make_album("don moen", "Grace"))
