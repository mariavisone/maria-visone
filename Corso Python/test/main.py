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
controllo.registro_accessi(d1)
controllo.registro_accessi(d2)
controllo.registro_accessi(d3)

#show il registro 
controllo.mostra_info()
