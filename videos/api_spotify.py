# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:16:07 2020

@author: BI
"""

url_base = 'https://api.spotify.com/v1'
ep_artist = '/artists/{artist_id}'
id_lebron = '3MeSOWo9ZSTe5Esf66uXam'

url_base+ep_artist.format(artist_id = id_lebron)

import requests
r = requests.get(url_base+ep_artist.format(artist_id = id_lebron))

r.status_code

r.json()
token_url = 'https://accounts.spotify.com/api/token'
params = {'grant_type': 'client_credentials'}
headers = {'Authorization' : 'Basic ZmViODA1OTAwNTEyNDQ4NDhiNTQ5NjYxOGVjYWIyMDE6OTNjM2Q4MzNhYmRhNGM2ZGE0YTEyMzA1NDQ2Yzg0MTc='}

r = requests.post(token_url, data=params, headers=headers)
r.status_code

r.json()

token = r.json()['access_token']
header = {'Authorization': 'Bearer {}'.format(token)}

r = requests.get(url_base+ep_artist.format(artist_id = id_lebron), headers = header)

r.status_code

r.json()


url_search = 'https://api.spotify.com/v1/search'

search_params = {'q':'Lebron+brothers', 'type': 'artist','market':'CO'}

busqueda = requests.get(url_search, headers= header,params=search_params)
busqueda.status_code

busqueda.json()