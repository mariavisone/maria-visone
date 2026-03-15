'''Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto
#poi Dare la possibilità all'utente di:
- modificare voti e alunni;
- eliminare alunni.
'''

#STEP da fare:
#funzione che crea - crea un file come database
#funzione che legge - leggi il file 
#creare il main - 



FILE_NAME = r"Mercoledì 18\Mattina\esercizio2_gruppo.py/students.csv"

# funzioni per scrivere
def write_file(s):
    with open(FILE_NAME, "w") as f:
        f.write(s)


# funzione per aggiungere
def append_file(s):
    with open(FILE_NAME, "a") as f:
        f.write(s)


# funzione per leggere
def read_file():
    with open(FILE_NAME,"r") as file:
        contenuto = file.read()
    return contenuto

def header():
    try:
        header = read_file().splitlines()[0]  # Legge la prima riga del file
        return header
    except FileNotFoundError:
        return None
    
def id_generator():
    try:
        lines = read_file().splitlines()
        if len(lines) > 1:
            last_id = int(lines[-1].split(",")[0])  # Prende l'ID dell'ultimo alunno
            return last_id + 1
        else:
            return 1  # Se il file è vuoto, inizia con ID 1
    except FileNotFoundError:
        return 1  # Se il file non esiste, inizia con ID 1

# ottimizzare la funzione per modificare alunni e voti
def modif_alunni():

    righe= read_file().splitlines() 

    if len(righe) <=1:
        print ("databbse vuoto")
        return 

    id_da_modicare= int(input("inserisci id di aluns modf: "))

    trovato= False 

# ciclo per trovare l'id da modificare per ora O(n) modificare in O(1)
    for i in range(1,len(righe)):
        colonne= righe[i].split(",")

        if int(colonne[0]) == id_da_modicare:
           trovato= True
           print(f"modifica in corso per {colonne[1]}")


           new_nome= input("inserisci il nuovo nome o lascia vuoto:  ")

           if new_nome =="":
               new_nome = colonne[1]


           new_voti= input("inserisci il nuovo voto o lascia vuoto, e separali con  (-)")
           if new_voti=="":
            new_voti= colonne[2]


           list_grades = new_voti.split("-")
           average = sum(map(float, list_grades)) / len(list_grades) if len(list_grades) > 0 else 0
           average = round(average, 2)


           righe[i]= f"{colonne[0]},{new_nome},{'-'.join(list_grades)},{average}"
           break


    if trovato:
        write_file("\n".join(righe))
        print("salvato")

    else:
        print("id non trovato")\


#funzione per eliminare
# ottimizzare la funzione
def delete_student():
    # Leggiamo tutte le righe dal file
    righe = read_file().splitlines()

    # Se c'è solo l'intestazione o il file è vuoto, inutile continuare
    if len(righe) <= 1:
        print("Database vuoto o file mancante.")
        return

    id_input = input("Inserisci l'ID dell'utente da eliminare: ")

    try:
        id_da_eliminare = int(id_input)
    except ValueError:
        print("Errore: devi inserire un numero.")
        return

    nuova_lista_righe = []
    trovato = False

    for riga in righe:
        # Se è la riga dell'intestazione (header), la salviamo sempre
        if riga.startswith("ID"): 
            nuova_lista_righe.append(riga)
            continue
        
        # Scomponiamo la riga per leggere il vero ID scritto nel file
        colonne = riga.split(",") 
        id_corrente = int(colonne[0])

        # Se l'ID corrisponde, NON lo aggiungiamo alla nuova lista (lo cancelliamo)
        if id_corrente == id_da_eliminare:
            trovato = True
            print(f"Eliminazione di: {colonne[1]}") # Feedback utile
        else:
            # Se non è quello da cancellare, lo teniamo
            nuova_lista_righe.append(riga)

    if trovato:
        # Riscriviamo il file con la lista aggiornata
        write_file("\n".join(nuova_lista_righe))
        print("Alunno eliminato e database aggiornato.")
    else:
        print("ID non trovato.")


while True:
    list_grades = []
    
    if header() is None:
        write_file("ID,Studente,Voti,Media")  # Crea il file con l'intestazione se non esiste

    s = input("\nCosa vuoi fare? \n(0) Uscire\n(1) Leggere elenco alunni\n(2) Aggiungere alunno\n(3) Eliminare alunno\n(4) Modificare alunno\nScelta: ")
    
    match s:
        case "0":
            print("\nUscita in corso...")
            break

        case "1":
            #ottimizzarte la stampa dell output
                r = read_file()
                print("\n",r)

        case "2":
             name = input("Inserisci il nome completo dell'alunno: ")
             while True:
                 grades = input("inserisci un voto per l'alunno (o invio per terminare): ")
                 if grades == "":
                    break
                 else:
                    list_grades.append(grades)

             average = sum(map(float, list_grades)) / len(list_grades) if len(list_grades) > 0  else 0
             average = round(average, 2)  # Arrotonda la media a 2 decimali
             student_info = f"\n{id_generator()},{name},{'-'.join(list_grades)},{average}"
             
             append_file(student_info)

        case "3":
            while True:
                confirm = input("Sei sicuro di voler eliminare un alunno? (s/n): ")
                if confirm.lower() == "s":
                    delete_student()
                
                elif confirm.lower() == "n":
                    print("Operazione annullata.")
                    break
                
                else:
                    print("Input non valido. Riprova.")

        case "4":
            while True:
                confirm = input("Sei sicuro di voler modificare un alunno? (s/n): ")
                if confirm.lower() == "s":
                    modif_alunni()
                    
                elif confirm.lower() == "n":
                    print("Operazione annullata.")
                    break
                
                else:
                    print("Input non valido. Riprova.")
            

        case _:
            print("Scelta non valida. Riprova.")
