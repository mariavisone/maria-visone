"""
================================================================================
AI-GUARD V2: ULTRALYTICS-POWERED SURVEILLANCE
================================================================================
Questo script usa il motore di Ultralytics (YOLOv11) per il tracking (seguimento
delle persone) e la libreria face_recognition (basata su Dlib) per la biometria.

SCOPO DIDATTICO:
Questo script è progettato per dimostrare come combinare l'Object Tracking ad 
alte prestazioni con il Riconoscimento Facciale Biometrico, ottimizzando le 
risorse hardware.

Nota: Se cv2.imshow (l'interfaccia grafica per mostrare il video) continua a fallire,
lo script ha un meccanismo di "fallback" che salverà l'output in un file video 
(.mp4) senza crashare.
================================================================================
"""

# Importiamo le librerie necessarie per interfacciarsi con il sistema operativo
import os

# OpenCV (cv2) è la libreria fondamentale per leggere dalla webcam e manipolare le immagini (frame)
import cv2

# NumPy (np) gestisce le matrici numeriche (i frame video sono matrici di pixel)
import numpy as np

# PyTorch (torch) è il motore di Deep Learning (Backend) che useremo per accelerare i modelli
import torch

# Dalla libreria ultralytics importiamo la classe YOLO, che ci permette di usare modelli YOLO
from ultralytics import YOLO

# Libreria per l'estrazione e il confronto degli "Embeddings" (Impronte Biometriche)
import face_recognition

# --- CONFIGURAZIONE AMBIENTE ---
# Diciamo a Keras (se viene usato indirettamente) di utilizzare PyTorch come motore sottostante.
# Questo è utile per garantire che tutta l'infrastruttura di AI usi la GPU in modo efficiente.
os.environ["KERAS_BACKEND"] = "torch"


def get_face_encodings(frame):
    """
    Funzione di supporto per estrarre gli "Encoding Biometrici" (Embeddings) da un frame.
    
    Cos'è un Encoding? È un vettore di 128 numeri che rappresenta univocamente 
    le proporzioni geometriche di un volto.
    
    Args:
        frame: L'immagine da analizzare (nel formato BGR tipico di OpenCV).
    Returns:
        Una lista di encodings (uno per ogni volto trovato nell'immagine).
    """
    # OpenCV usa di default lo spazio colore BGR (Blue, Green, Red).
    # Tuttavia, la libreria face_recognition è basata su Dlib, che richiede lo spazio RGB.
    # Quindi, la prima cosa da fare è convertire i colori.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Restituisce il vettore matematico che descrive il volto
    return face_recognition.face_encodings(rgb_frame)


def main():
    """
    Funzione principale che esegue l'intera pipeline:
    Fase 1: Registrazione (Enrollment) dei volti autorizzati.
    Fase 2: Sorveglianza (Tracking + Face Recognition).
    """
    
    # --------------------------------------------------------------------------
    # FASE 1: REGISTRAZIONE UTENTI (ENROLLMENT)
    # --------------------------------------------------------------------------
    print("\n--- AI-GUARD: REGISTRAZIONE UTENTI ---")
    
    # Preparo due liste vuote. 
    # - known_encodings conterrà i vettori numerici (le facce).
    # - known_names conterrà i nomi associati a quei vettori.
    known_encodings = []
    known_names = []
    
    # Chiedo all'utente quante persone inserire nel database degli autorizzati
    try:
        n = int(input("Quanti utenti vuoi registrare? "))
    except: 
        # Se l'utente non inserisce un numero, gestiamo l'errore senza crashare
        n = 0

    # Inizializzo l'oggetto VideoCapture di OpenCV per leggere dalla webcam (Device ID 0)
    cap = cv2.VideoCapture(0)
    
    # Eseguo un ciclo per registrare ogni persona
    for i in range(n):
        nome = input(f"Registrazione persona {i+1}. Premi 'C' per catturare: ")
        
        # Loop infinito per mostrare il flusso video finché l'utente non preme 'C'
        while True:
            # .read() restituisce 'ret' (booleano: vero se ha letto il frame) e 'frame' (l'immagine)
            ret, frame = cap.read()
            if not ret: 
                break # Esco dal loop se la webcam si scollega o fallisce
            
            # Scrivo del testo in sovrimpressione sul video per dare feedback all'utente
            cv2.putText(frame, f"Registrando {nome}. Premi 'C'", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            
            # Provo a mostrare la finestra. 
            cv2.imshow("Registrazione", frame)
            
            # cv2.waitKey(1) aspetta 1 millisecondo e controlla se la tastiera è stata premuta.
            # & 0xFF == ord('c') controlla se il tasto premuto è esattamente la lettera 'c' minuscola.
            if cv2.waitKey(1) & 0xFF == ord('c'):
                
                # Se è stata premuta 'c', calcolo l'impronta biometrica
                encs = get_face_encodings(frame)
                
                # Controllo se è stato trovato almeno un volto (len_encs > 0)
                if len(encs) > 0:
                    # Salvo il primo volto trovato (encs[0]) nella lista degli autorizzati
                    known_encodings.append(encs[0])
                    # Salvo il nome associato
                    known_names.append(nome)
                    print(f"OK! {nome} registrato.")
                    # Esco dal loop 'while' di questa persona, passando alla successiva
                    break
    
    # Terminata la registrazione, distruggo le finestre OpenCV e rilascio la webcam per sicurezza
    cv2.destroyAllWindows()
    cap.release()
    
    
    # --------------------------------------------------------------------------
    # FASE 2: SORVEGLIANZA CON TRACKING
    # --------------------------------------------------------------------------
    print("\n--- AI-GUARD: AVVIO SORVEGLIANZA (ULTRALYTICS) ---")
    
    # Inizializzo il modello YOLOv11 nano. "n.pt" indica il modello base molto rapido (Nano).
    # YOLO scaricherà il modello automaticamente la prima volta.
    model = YOLO("yolo11n.pt")
    
    # Avvio la funzione di tracking sui frame della webcam (source="0").
    # * show=False: Diciamo a YOLO di NON provare ad aprire una finestra da solo.
    # * stream=True: Restituisce un costrutto 'generatore' per gestire i frame uno per volta senza riempire la RAM.
    # * persist=True: ATTIVA L'OBJECT TRACKING. Assegnerà lo stesso ID a una persona finché è nell'inquadratura.
    # * classes=[0]: Filtra tutti gli oggetti a parte la classe 0 (Persona).
    results = model.track(source="0", show=False, stream=True, persist=True, classes=[0])
    
    # id_to_name è una "memoria a breve termine". 
    # Struttura: { Track_ID_YOLO : "Nome Riconosciuto" }
    # Ci serve perché, avendo il Tracking di YOLO, non dobbiamo calcolare il riconoscimento facciale ad ogni frame, 
    # ma solo la priva volta che compare un nuovo ID! Questo fa risparmiare moltissima CPU/GPU!
    id_to_name = {}

    # Variabili per gestire il salvataggio su file video se non c'è lo schermo (headless)
    video_writer = None
    headless_mode = False
    print("\n[INFO] Sorveglianza avviata. Se la finestra non appare, il sistema salverà un video 'output_surveillance.mp4'.")

    # Questo è il cuore del programma. Scorre i frame analizzati in tempo reale da YOLO.
    for r in results:
        # Recupero l'immagine originale a colori
        frame = r.orig_img.copy()
        
        # Le "boxes" sono i rettangoli trovati da YOLO. Controlliamo che abbiano un ID (perché stiamo tracciando).
        if r.boxes.id is not None:
            # Estraggo le coordinate [x_sinistra, y_alta, x_destra, y_bassa] per tutti i box trovati
            boxes = r.boxes.xyxy.cpu().numpy().astype(int)
            # Estraggo i tracking IDs corrispondenti
            ids = r.boxes.id.cpu().numpy().astype(int)
            
            # Analizzo ogni persona rilevata iterando su coordinate e relativo ID in parallelo
            for box, track_id in zip(boxes, ids):
                
                # **********************************************
                # LOGICA DI EFFICIENZA INTELLIGENTE (SOTA 2026)
                # **********************************************
                # Se l'ID è sconosciuto, non sappiamo chi sia. 
                # Solo in questo caso eseguiamo il pesante calcolo del riconoscimento facciale.
                if track_id not in id_to_name:
                    x1, y1, x2, y2 = box # Destrutturo l'array
                    
                    # Recupero dalla foto intera solo la regione di interesse (Face/Person ROI) usando "slicing"
                    face_roi = frame[y1:y2, x1:x2]
                    
                    # Controllo che la box ritagliata non sia vuota
                    if face_roi.size > 0:
                        # Estrazione dell'impronta facciale dalla sola foto ritagliata
                        encs = get_face_encodings(face_roi)
                        
                        # Se ha individuato dei connotati biometrici...
                        if encs:
                            # Confrontiamo il nuovo volto (encs[0]) contro il database degli autorizzati.
                            # tolerance=0.5 è la pignoleria: 0.0 è severissimo, 1.0 accetta chiunque.
                            matches = face_recognition.compare_faces(known_encodings, encs[0], tolerance=0.5)
                            
                            # Matches restituisce un array di booleani (es. [False, True, False])
                            # Se c'è almeno un "True"...
                            if True in matches:
                                # Trovo l'indice del True per pescare il nome nell'array corrispondente
                                matched_index = matches.index(True)
                                # Associo finalmente l'ID tracciato spazialmente al nome Biometrico!!
                                id_to_name[track_id] = known_names[matched_index]
                            else:
                                # Sconosciuto biometricamente.
                                id_to_name[track_id] = "SCONOSCIUTO" # se è sconosciuto per 3 secondi di fila
                                # manda un allarme
                
                # --- DISEGNO A SCHERMO ---
                
                # Prendo il nome dalla memoria (oppure di default "Analisi..." se ancora non è finito)
                name = id_to_name.get(track_id, "Analisi...")
                x1, y1, x2, y2 = box # Ricreo le coordinate
                
                # Diamo uno stile semantico a colori a seconda dell'identità:
                # Verde (0, 255, 0) se Autorizzato, Rosso (0, 0, 255) se Sconosciuto.
                color = (0, 255, 0) if name not in ["SCONOSCIUTO", "Analisi..."] else (0, 0, 255)
                
                # Disegno un rettangolo colorato attorno alla persona (box spessa 2 pixel)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                
                # Disegno il testo per etichettare la persona includendo TrackID (spessore testo 2)
                cv2.putText(frame, f"{name} (ID:{track_id})", (x1, y1-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Aggiungo a tutti i frame la "filigrana" in basso a sinistra
        cv2.putText(frame, "SCUOLA 2026 - AI GUARD", (10, frame.shape[0] - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # ----------------------------------------------------------------------
        # GESTIONE DISPLAY / MODALITÀ HEADLESS (FALLBACK)
        # Se si esegue lo script su terminali in remoto o se l'ambiente ha bug grafici,
        # cv2.imshow genererà un'eccezione. Dobbiamo proteggerci per evitare che l'allarme
        # smetta di monitorare solo perché non si apre uno scherma visivo.
        # ----------------------------------------------------------------------
        if not headless_mode: # Se supponiamo di avere ancora la GUI attiva
            try:
                # Provo ad aprire un player video "AI-GUARD SURVEILLANCE"
                cv2.imshow("AI-GUARD SURVEILLANCE", frame)
                
                # Permetto chiusura premendo il tasto Q (esci dal for loop principale)
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break 
            except Exception: # Se l'istruzione precedente fallisce...
                print("\n[WARNING] Impossibile trovare un'interfaccia grafica. Attivo salvataggio su File (modalità headless).")
                headless_mode = True
                
                # Configuro l'encoder Video mp4 in OpenCV
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                h, w = frame.shape[:2] # Altezza e larghezza
                
                # Dichiaro il file writer indicando NomeFile, Encoder, Framerate FPS (20fps), (GrandezzaFinestra)
                video_writer = cv2.VideoWriter('output_surveillance.mp4', fourcc, 20.0, (w, h))

        # Se sono finito o se ero già in headless mode... scrivo i bit su disco fisico
        if headless_mode and video_writer:
            video_writer.write(frame)
            # Produco un punto in shell ogni frame processato come riscontro vitale
            print(".", end="", flush=True) 

    # Usciti dal ciclo (per stop da utente o fine flusso webcam), rilascio formalmente il file mp4 per permettere l'apertura in VLC
    if video_writer:
        video_writer.release()
        print("\n\n[INFO] Sorveglianza terminata. Il log video analitico è stato riassunto fedelmente in 'output_surveillance.mp4'")
    
    # Pulizia memoria video
    cv2.destroyAllWindows()

# Punto d'ingresso "Main" dello script
if __name__ == "__main__":
    main()
