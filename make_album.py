
def make_album(artist_name, album_title, tracks=""):
	
	album = {"artist_name": artist_name.title(), "album_title": album_title.title()}
	if tracks:
		album["tracks"] = tracks

	return album

while True:

	print("Press q at anytime to quit!")

	art_name = raw_input("Enter Artist Name: ")
	if art_name == 'q':
		break

	alb_title = raw_input("Enter Album Name: ")
	if alb_title == 'q':
		break

	print(make_album(artist_name = art_name , album_title = alb_title ))