def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

album = make_album('The Beatles', 'Abbey Road')
print(album)

album = make_album('The Rolling Stones', 'Sticky Fingers')
print(album)

album = make_album('The Who', 'Tommy', 11)
print(album)
