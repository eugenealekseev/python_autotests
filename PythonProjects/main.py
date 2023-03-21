import requests

token='6a646635d870df35bae75997ffabbaf2'
add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons' , headers = {'Content-Type' : 'application/json', 
                                                                                           'trainer_token' : token},
                                                                                           json={
                                                                                           "name": "КуКу",
                                                                                           "photo": "https://dolnikov.ru/pokemons/albums/010.png"
                                                                                            })
print(add_pokemon_response.text)


new_name_pokemon = requests.put('https://pokemonbattle.me:9104/pokemons' , headers = {'Content-Type' : 'application/json', 
                                                                                           'trainer_token' : token},
                                                                                           json={
                                                                                           "pokemon_id": 6361,
                                                                                           "name": "КуКу2",
                                                                                           "photo": "https://dolnikov.ru/pokemons/albums/010.png"
                                                                                            })
print(new_name_pokemon.text)


pokeball_pokemon = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball' , headers = {'Content-Type' : 'application/json', 
                                                                                           'trainer_token' : token},
                                                                                           json={
                                                                                           "pokemon_id": 6366
                                                                                           })

print(pokeball_pokemon.text)