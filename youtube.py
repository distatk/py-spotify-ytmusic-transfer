from ytmusicapi import YTMusic

ytmusic = YTMusic("auth.json")

def search_song(search_string):
    return ytmusic.search(query=search_string, filter='songs')

def add_song_to_playlist(token):
    ytmusic.edit_song_library_status(token)

def add_song(search_string):
    search_result = search_song(search_string)
    if (search_result):
        add_token = search_result[0]['feedbackTokens']['add']
        if (add_token):
            add_song_to_playlist(add_token)
            print('added ' + search_result[0]['title'] + ' - ' + search_result[0]['artists'][0]['name'])