from ytmusicapi import YTMusic

ytmusic = YTMusic("auth.json")

def search_song(search_string):
    return ytmusic.search(query=search_string, filter='songs')

def add_song_to_playlist(token):
    ytmusic.edit_song_library_status(token)

def like_song(video_id):
    ytmusic.rate_song(videoId=video_id, rating='LIKE')

def add_song(search_string):
    search_result = search_song(search_string)
    if (search_result):
        print(search_result[0]['videoId'])
        video_id = search_result[0]['videoId']
        if (video_id):
            like_song(video_id)
            print('added ' + search_result[0]['title'] + ' - ' + search_result[0]['artists'][0]['name'])