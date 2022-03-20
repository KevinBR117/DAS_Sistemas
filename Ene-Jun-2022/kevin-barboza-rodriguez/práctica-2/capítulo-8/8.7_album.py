def make_album(artist_name, album_title, tracks=''):
    dict_album = {'artist': artist_name, 'album': album_title }
    if tracks:
        dict_album['tracks'] = tracks
    return dict_album

print(make_album("Natalia lafourcade", "Huhuhu"))
print(make_album("Avicii", "True stories"))
print(make_album("Kygo", "Cloud nine", "9"))    