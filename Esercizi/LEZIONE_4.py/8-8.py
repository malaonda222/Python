# Album utente
# def make_album(artista:str, titolo:str) -> dict[str, str]:
#         album = {"nome": artista, "album": titolo}
#         return album

# while True:
#     scelta = input("Would you like to insert an artist and the album of the artist? If no, write quit: ")
#     if scelta == "quit".lower():
#         print("Il programma si interrompe.")
#         break
#     else:
#         artist = input("Insert the artist: ")
#         nome_album = input("Insert the album name: ")

#     album_1 = make_album(artist, nome_album)
#     print(album_1)



def make_albums(artist_name:str, album_title:str) -> dict[str]:
    info_artista = {"nome": artist_name, "album": album_title}
    return info_artista

while True:
    opzione = input(f"Vuoi inserire un artista e il suo album? Se no, digitare \"si\" oppure \"no\": ")
    if opzione == "no".lower():
        print("Il programma termina.")
        break
    if opzione == "si".lower():
        artist_name = input("Inserisci il nome dell'artista: ")
        album_title = input("Inserisci il nome dell'album: ")
        print(make_albums(artist_name, album_title))   
    else:
        print("Errore. Input non riconosciuto, riprovare.")
        continue
        