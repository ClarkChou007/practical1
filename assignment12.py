sing = ''
for i in range(1,7):
    sing += str(i)
for j in range (6):
    songs = sing[j:]+sing[:j]
    print(songs)

