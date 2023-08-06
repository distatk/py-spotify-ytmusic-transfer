import spotify as sptfy
import youtube as ytb

songs_per_query = 20

sptfy.create_spotify_client()

i = 45
while True: 
    music_name_list = sptfy.get_saved_tracks(limit=songs_per_query, offset=i * songs_per_query)
    print('music_name_list', music_name_list)
    for item in music_name_list:
        ytb.add_song(item)

    if (len(music_name_list) < songs_per_query):
        break
    i+=1

