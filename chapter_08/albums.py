def make_album(name, title, track = None):
    album = {'musician': name, 'title': title}
    if track:
        album['track'] = track
    return album

while True:
    username = input("\nWhat is your name? ")
    if username == 'q':
        break
    text = "(enter 'q' to any time to quit)"

    m_name = input("Musician: ")
    if m_name == 'q':
        break
    a_title = input("Album: ")
    if a_title == 'q':
        break

    full_album = make_album(m_name, a_title)
    print(f"Hello, {username}, see next info:")
    print(full_album)



# musician = make_album('kino', 'noch')
# print(musician)
#
# musician = make_album('kino', 'noch', 27)
# print(musician)