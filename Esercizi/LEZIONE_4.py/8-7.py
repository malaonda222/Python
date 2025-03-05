# Album
def make_album(artist:str, album_title:str, song=None) -> dict[str, str, int]:
    return {"artist_name": artist, "album": album_title, "canzoni":song}

print(make_album("Lisa", "Pythonando"))
print(make_album("Mahmood", "Gioventù bruciata", 8))
print(make_album("Lady Gaga", "The Fame", 10))
