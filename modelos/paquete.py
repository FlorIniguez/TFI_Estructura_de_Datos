from estructuras.arbol_general import ArbolGeneral

class Paquete:
    def __init__(self, id_paquete,peso,prioridad,origen,destino):
        self.id_paquete = id_paquete
        self.peso = peso
        self.prioridad = prioridad # 1 urgente, 2 normal, 3 baja
        self.orginen = origen
        self.destino = destino
        #Aca creo la raiz del arbol, es como una carpeta principal
        self.historial = ArbolGeneral("Historial del paquete")
        
    def __str__(self):
        return f"Paquete {self.id_paquete} - Prioridad {self.prioridad}"