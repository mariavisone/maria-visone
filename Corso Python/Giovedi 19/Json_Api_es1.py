"""Create un programma python che permette tramite le api di visualizzare le previsione
metereologiche della città scelta dall'utente.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni."""
    
import requests
import webbrowser

# Chiedi all'utente il nome della città
citta = input("Quale città vuoi cercare? ").capitalize().strip()
    
# Componi l'URL (usa le f-string per inserire la variabile 'citta')
url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"
    
# Invia la richiesta al sito
risposta = requests.get(url_geo)
    
# Trasforma la risposta in un dizionario (JSON)
dati = risposta.json()
    
# Per ora stampiamo i dati per vedere se funziona
print(dati)

# Chiedi i dettagli all'utente
giorni = input("Per quanti giorni vuoi le previsioni? (1, 3, 7): ")
vuoi_vento = input("Vuoi vedere la velocità del vento? (s/n): ")
vuoi_pioggia = input("Vuoi vedere le precipitazioni? (s/n): ")

risultato = dati["results"][0]

lat = risultato["latitude"]
lon = risultato["longitude"]
timezone = risultato["timezone"]

# Ora iniziamo a costruire l'URL per il meteo usando le variabili lat e lon
url_meteo = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&forecast_days={giorni}&timezone=auto&daily=temperature_2m_max,temperature_2m_min"

# Se l'utente ha risposto 's', aggiungiamo il pezzetto del vento all'indirizzo
if vuoi_vento == 's':
    url_meteo += ",windspeed_10m_max"

# Se l'utente vuole la pioggia, aggiungiamo anche quella
if vuoi_pioggia == 's':
    url_meteo += ",precipitation_sum"

"""# Alla fine chiudiamo l'URL con i giorni scelti e il fuso orarioro
url_meteo += f"&forecast_days={giorni}&timezone=auto"""

nuova_risposta = requests.get(url_meteo)

nuovi_dati = nuova_risposta.json()

#print(nuovi_dati)

#webbrowser.open(url_meteo)
previsioni = nuovi_dati["daily"]
        
for i in range(len(previsioni["time"])):
    giorno = previsioni["time"][i]
    t_max = previsioni["temperature_2m_max"][i]
    t_min = previsioni["temperature_2m_min"][i]
    
    output = (f"Giorno: {giorno}, Temperatura max:{t_max}°C, Temperatura min: {t_min}°C")
    
    if "windspeed_10m_max" in previsioni:
        windspeed = previsioni["windspeed_10m_max"][i]
        output += (f" Vento: {windspeed} km/h")
        
    if "precipitation_sum" in previsioni:
        pioggia = previsioni["precipitation_sum"][i]
        output += (f" Precipitazioni: {pioggia} mm")
        
    print(output)
    #print(f"giorno {dati["time"][i]} temperatura:{dati["temperature_2m"][i]}")
    
    """for i in range(len(previsioni["time"])):
    giorno = previsioni["time"][i]
    t_max = previsioni["temperature_2m_max"][i]
    t_min = previsioni["temperature_2m_min"][i]
    
    output = f"Giorno: {giorno} | Temp: {t_min}°/{t_max}°C"
    
    # Verifica la chiave esatta
    if "windspeed_10m_max" in previsioni:
        output += f" | Vento: {previsioni['windspeed_10m_max'][i]} km/h"
        
    if "precipitation_sum" in previsioni:
        output += f" | Pioggia: {previsioni['precipitation_sum'][i]} mm"
        
    print(output)"""