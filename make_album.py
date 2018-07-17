
def make_album(artist_name, album_title, tracks=""):
	
	album = {"artist_name": artist_name.title(), "album_title": album_title.title()}
	if tracks:
		album["tracks"] = tracks

	return album

print(make_album(artist_name ="flavour", album_title = "divine", tracks = 5))
print(make_album(artist_name = "don moen", album_title = "Grace"))
