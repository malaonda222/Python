# Album
def make_album(artist:str, album_title:str, song=None) -> dict[str, str, int]:
    return {"artist_name": artist, "album": album_title, "canzoni":song}

print(make_album("Lisa", "Pythonando"))
print(make_album("Mahmood", "Gioventù bruciata", 8))
print(make_album("Lady Gaga", "The Fame", 10))





def make_album(artist_name:str, album_title:str): 
    return {"artist": artist_name, "album": album_title}

artist_1 = make_album("Shakira", "New")
print(artist_1)
artist_2 = make_album("Jovanotti", "Vita")
print(artist_2)
artist_3 = make_album("Venerus", "Musica magica")
print(artist_3)


def make_albums(artist_name:str, album_title:str, canzoni=None) -> dict[str, str, int]: 
    return {"artist": artist_name, "album": album_title, "songs": canzoni}

artist_4 = make_albums("Marco Mengoni", "Due vite", 50)
print(artist_4)
