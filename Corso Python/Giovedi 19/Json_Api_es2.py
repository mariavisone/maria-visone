'''Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), 
in caso non fosse presente vi permetterà di catturarlo 
salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 pokemon)

https://pokeapi.co/

https://pokeapi.co/docs/v2  '''

import requests
import random
import json

# CONFIGURAZIONE E PREPARAZIONE ALBUM 
FILE_NAME = "pokedex.json"  # nome del file dove salveremo i pokemon

def carica_pokedex():
    try:   # provo a leggere il file  se da errore allora lo trasformo in dizionario
        with open(FILE_NAME, "r") as file:
            pokedex = json.load(file)
        print("pokedex pronto!")
    except:
        pokedex = {}   # se non esiste mi creo un dizionario vuoto
        print("pokedex caricato", pokedex)
    return pokedex

#  FUNZIONI DI SUPPORTO 
def pokemon_info(dex_number):
    # url del sito, inserire id or name
    url_pokedex = f"https://pokeapi.co/api/v2/pokemon/{dex_number}"
    
    try:
        # invio richiesta al sito per vedere se funzionava
        response = requests.get(url_pokedex)
        
        if response.status_code == 200:
            raw_data = response.json() #prende file json
            print(f"Dati grezzi ricevuti per: {raw_data['name']}") # debug
           
            pokemon_data = { #filtrato 
                "nome": raw_data["name"],
                "pokedex_N°": raw_data["id"],
                "type": [t["type"]["name"] for t in raw_data["types"]]
            }
            return pokemon_data
        else:
            print("Errore: Pokémon is MissingNO")
            return None
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return None

def eCatturato(id_pkmn, pkdex):
    # controllo se l'id (come stringa) è presente nelle chiavi del dizionario
    if str(id_pkmn) in pkdex.keys():
        return True
    else:
        return False

#  MAIN PROGRAM (ESECUZIONE) ---
pokedex = carica_pokedex()

while True:
    id_pokemon = random.randint(1, 1025)
    print(f"\nè apparso il pokemon {id_pokemon}")

    # controllo se il pokemon è già nell'album (pokedex)
    if eCatturato(id_pokemon, pokedex) == True:
        print("Questo Pokémon è già stato catturato!.")
        #print("Vuoi provare a catturare un altro esemplare?.")
        
    else: 
        print("Questo Pokémon non è stato catturato!.")
        print("Lo cerco su internet...")
        
        # recupero i dati tramite la funzione pokemon_info
        pokemon = pokemon_info(id_pokemon)
        
        if pokemon:
            print(f"Hai incontrato {pokemon['nome'].capitalize()}!")
            print("Tipo:", ", ".join(pokemon["type"]))
            scelta = input("Vuoi catturarlo? [Si] o [No]: ").lower() 

            if scelta == "si":
                # aggiungo il pokemon al pokedex usando l'id come chiave
                pokedex[str(id_pokemon)] = pokemon
                
                # salvataggio permanente sul file
                with open(FILE_NAME, "w") as f:
                    json.dump(pokedex, f, indent=4)
                print(f"Preso! {pokemon['nome']} salvato nel pokedex.")
            else:
                print("Scampato Pericolo!")
    uscita = input ("Vuoi continuare a giocare?") 
    if uscita.lower() == "no" :
        print("Grazie per aver giocato")
        break





#Maria
'''import requests
import random
import json   #serve per lavorare con il file json

FILE_NAME = "pokedex.json"  #nome del file dove salveremo i pokemon

#preparazione album
def carica_pokedex():
    try:   #provo a legger il file- se da errore allora lo trasformo in dizionario
        with open (FILE_NAME, "r") as file:
            pokedex = json.load(file)
        print("pokedex pronto!")
    except:
        pokedex = {}   #se non eiste mi creo un dizionario vuoto che contenga tutto uello che catturo
        print("pokedex caricato" , pokedex)
    return pokedex

    #---main
    pokedex = carica_pokedex()

    #stampa veloce per controllare
    print(pokedex)'''

#Giovanni
'''pokedex = carica_pokedex()

for i in range(5):
    id_pokemon = random.randint(1, 1025)
    print(f"\nincontro numero {i+1}: è apparso il pokemon {id_pokemon}")

    # controllo se il pokemon è già nell'album (pokedex)
    if eCatturato(id_pokemon, pokedex) == True:
        print("Questo Pokémon è già stato catturato!.")
        print("Vuoi provare a catturare un altro esemplare?.")
        continue 
    else: 
        print("Questo Pokémon non è stato catturato!.")
        print("Lo cerco su internet...")
        
        # recupero i dati tramite la funzione pokemon_info
        pokemon = pokemon_info(id_pokemon)
        
        if pokemon:
            print(f"Hai incontrato {pokemon['nome'].capitalize()}! Vuoi catturarlo?.")
            scelta = input("Scegli [S] o [N]: ").lower()

            if scelta == "s":
                # aggiungo il pokemon al pokedex usando l'id come chiave
                pokedex[str(id_pokemon)] = pokemon'''


#Gabriele
'''def eCatturato(id_pkmn, pkdex):
    if id_pkmn in pkdex.keys():
        return True
    else:
        return False


pokedex = {} #
pokemon = "Bulbasaur" # 

id_pokemon = pokemon["id"]

if eCatturato(pokemon, pokedex) == True:
    print("Questo Pokémon è già stato catturato!.")
    print("Vuoi provare a catturare un altro esemplare?.")
else: 
    print("Questo Pokémon non stato catturato!.")
    print("Vuoi catturarlo?.")

scelta = int(input("Scegli [S] o [N]"))

if scelta == "s":
    pokedex[id] = pokemon
else:
    print("Scampato Pericolo!")'''


#Davide
'''from random import randint
import requests
import json

dex_number = randint(1, 1008) 

def pokemon_info(dex_number):

    #url del sito, inserire id or name
    url_pokedex = f"https://pokeapi.co/api/v2/pokemon/{dex_number}"
    
    try:
        # invio richiesta al sito
        response = requests.get(url_pokedex)
        
        if response.status_code == 200:
            raw_data = response.json()
            print(f"Dati grezzi ricevuti per: {raw_data['name']}")#debug
           
            pokemon_data = {"nome": raw_data["name"],
                            "pokedex_N°": raw_data["id"],
                          "type": [t["type"]["name"] for t in raw_data["types"]]}
                
            return pokemon_data
        
        else:
            print("Errore: Pokémon is MissingNO")
            return None
        
    except Exception as e:
        print(f"Errore di connessione: {e}")
        return None

pokemon_info(dex_number)'''