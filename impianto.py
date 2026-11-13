from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        
        self._codice = codice
        self._modello = modello
        self._localita = localita
        self._potenza_massima_kw = potenza_massima_kw
        self._stato = stato
        self._pannelli = list [PannelloFotovoltaico]
        
    def get_codice(self) -> str:
        return self._codice
        
    def set_codice(self, nuovo_codice: str):
        _codice = nuovo_codice
        
    def get_modello(self) -> str:
        return self._modello
    
    def set_modello(self, nuovo_modello: str):
        _modello = nuovo_modello
        
    def get_localita(self) -> str:
        return self._localita
    
    def set_localita(self, nuova_localita: str):
        _localita = nuova_localita
        
    def get_potenza_massima_kw(self, pannello: PannelloFotovoltaico ) -> float:
        if (pannello in self._pannelli):
            return pannello.potenza_kw
        else: print("Pannello non installato")
        
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico):
        pannelli.append(pannello)

    """
    def potenza_pannelli(self) -> float:
        potenza_massima = 0.0
        for(p in self._pannelli):
            potenza_massima += p.potenza_kw
        
        return potenza_massima
    
    def cerca_pannello(self, codice: str):
        for(p in self._pannelli):
            if(p.codice == codice):
                self._pannelli.remove(p)
            else: return None
    """
                
        
        