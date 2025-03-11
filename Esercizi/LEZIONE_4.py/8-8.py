# Album utente
def make_album(artista:str, titolo:str) -> dict[str, str]:
        album = {"nome": artista, "album": titolo}
        return album

while True:
    scelta = input("Would you like to insert an artist and the album of the artist? If no, write quit: ")
    if scelta == "quit".lower():
        print("Il programma si interrompe.")
        break
    else:
        artist = input("Insert the artist: ")
        nome_album = input("Insert the album name: ")

    album_1 = make_album(artist, nome_album)
    print(album_1)