import requests

url_base = "https://api.spotify.com/v1"

token_url = 'https://accounts.spotify.com/api/token'
params = {'grant_type': 'client_credentials'}
headers = {'Authorization' : 'Basic YzgyMjM4NDQ2Zjg3NGVhMTk1ZWY2NzUwYWRiNTNjZGI6MmUxMjcwMTk4MzY5NDQxMmEyN2NmNzU3NWRhNTI1OTc='}

r = requests.post(token_url, data=params, headers=headers)
dic_token = r.json()
token_user = dic_token['access_token']

#token = r.json()['access_token']
header = {'Authorization': 'Bearer {}'.format(token_user)}# what it is inside the brackets will be what it is inside format

url_search = f"{url_base}/search"
search_params = {'q':'lebron', 'type': 'artist','market':'CO'}
busqueda = requests.get(url_search, headers= header,params=search_params)
id_first_result = busqueda.json()['artists']['items'][0]['id']
params_market = {'market': 'CO'}
url_top_artists_songs = f"{url_base}/artists/{id_first_result}/top-tracks"

search_top_songs = requests.get(url_top_artists_songs, headers = header, params = params_market)
print(search_top_songs.json())