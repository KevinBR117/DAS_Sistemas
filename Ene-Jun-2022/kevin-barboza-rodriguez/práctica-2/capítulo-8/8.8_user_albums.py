def make_album(artist_name, album_title, tracks=''):
    dict_album = {'artist': artist_name, 'album': album_title }
    return dict_album

while True:
    print("Enter 'q' at any time to quit\n")

    artist_name = input("Enter a artist name: ")
    if artist_name == "q":
        break

    album_title = input("Enter an album title: ")
    if album_title == "q":
        break

    print()
    print(make_album(artist_name, album_title))
    print()