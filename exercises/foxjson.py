'''zorros = {"image":"https:\/\/randomfox.ca\/images\/36.jpg","link":"https:\/\/randomfox.ca\/?i=36"}

lista_de_zorros = zorros.keys()
print (lista_de_zorros)
zorros_lista = list(lista_de_zorros)
print (zorros_lista)

print(zorros_lista[1])

print(zorros[zorros_lista[1]])'''


lebron_json = {'external_urls': {'spotify': 'https://open.spotify.com/artist/3MeSOWo9ZSTe5Esf66uXam'}, 'followers': {'href': None, 'total': 84816}, 'genres': ['boogaloo', 'latin jazz', 'salsa', 'salsa international', 'tropical'], 'href': 'https://api.spotify.com/v1/artists/3MeSOWo9ZSTe5Esf66uXam', 'id': '3MeSOWo9ZSTe5Esf66uXam', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab6761610000e5eba105ee4a794f15dc8f78908f', 'width': 640}, {'height': 320, 'url': 'https://i.scdn.co/image/ab67616100005174a105ee4a794f15dc8f78908f', 'width': 320}, {'height': 160, 'url': 'https://i.scdn.co/image/ab6761610000f178a105ee4a794f15dc8f78908f', 'width': 160}], 'name': 'Lebrón Brothers', 'popularity': 48, 'type': 'artist', 'uri': 'spotify:artist:3MeSOWo9ZSTe5Esf66uXam'}

lebron_keys = lebron_json.keys()
#print (lebron_keys)
list_lebron_keys = list(lebron_keys)
print (list_lebron_keys)
print("A")
for lebron in list_lebron_keys:
    print (lebron_json[lebron])
print("B")
print (f" Artist name is {lebron_json[list_lebron_keys[6]]} ")  
print("c")
print(f"Artist's popularity is {lebron_json['popularity']}")  
print("d")
print (f"Artist's followers are {lebron_json['followers']['total']}")
print ("e")
print (f"second image's URL is {lebron_json['images'][1]['url']}")   
print ("f")
print (f"genre number 3 is {lebron_json['genres'][2]}")