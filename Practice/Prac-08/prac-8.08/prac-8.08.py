def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease enter the artist's name and the album's title.")
    print("(Enter 'q' at any time to quit.)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    print("Whether you want to add the number of tracks?(input -1 blank)")
    tracks = input("Tracks: ")
    if int(tracks) == -1:
        active = False
    else:
        active = True

    if active:
        album = make_album(artist, title, tracks)
    else:
        album = make_album(artist, title)
    
    print(album)