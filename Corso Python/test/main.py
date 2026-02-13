#main 
#importo le classi 
from utenti import Dipendente 
from Controlli import ControlloAccesso

#creo i dipendenti
d1 = Dipendente( "Maria Vis", "X00", "Mattina", "Desk")
d2 = Dipendente( "Mario tis", "X02", "Pomeriggio", "Assistente")
d3 = Dipendente( "luca Vit", "X03", "Mattina", "dottore")

#l'oggetto di controlloAccesso
controllo = ControlloAccesso()

#il registro ingressi
controllo.registra_ingresso(d1)
controllo.registra_ingresso(d2)
controllo.registra_ingresso(d3)

#show il registro 
controllo.mostra_info()
