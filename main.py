from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

class main:
    
    def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare):
        if (impianto in impianti):
            ValueError ("Impianto gia presente")
        else: return None
        
    def cerca_impianto (impianti: list[ImpiantoSolare], codice: str):