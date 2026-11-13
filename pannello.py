class PannelloFotovoltaico:
    
    def __init__(self, codice: str, modello: str, potenza_kw: float) -> None:
        self._codice = codice
        self._modello = modello
        self._potenza_kw = potenza_kw
        
    def get_codice(self) -> str:
        return self._codice
        
    def set_codice(self, nuovo_codice: str):
        _codice = nuovo_codice
        
    def get_modello(self) -> str:
        return self._modello
    
    def set_modello(self, nuovo_modello: str):
        _modello = nuovo_modello
        
    def get_potenza(self) -> float:
        return self._potenza_kw
    
    def set_modello(self, nuova_potenza_kw: str):
        if (nuova_potenza_kw > 0):
            _potenza_kw = nuova_potenza_kw
        else:
            print ("Potenza Non Valida")