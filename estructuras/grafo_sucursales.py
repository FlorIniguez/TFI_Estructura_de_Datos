class Grafo:
    """
    Representa la red de rutas entre sucursales mediante una lista de adyacencia.
    Cada nodo corresponde a una sucursal y sus conexiones (aristas) indican rutas dirigidas
    con un peso asociado (distancia en kilómetros).
    
    Esta estructura permite aplicar algoritmos como BFS, DFS y Dijkstra
    para obtener caminos, verificar conectividad y calcular rutas óptimas.
    """
    def __init__(self):
        self.adyacencias = []   # Lista de listas: cada nodo tiene su lista de vecinos

    def agregar_sucursal(self):
       #Cuando agrego una sucursal, simplemente agrego una lista vacía a la lista de adyacencia.
        #El índice donde se inserta esa lista es el ID de la sucursal.
        self.adyacencias.append([])  
        return len(self.adyacencias) - 1  # devuelve el ID  asignado al nuevo nodo

    def agregar_ruta(self, origen, destino, peso=1):
        """
        Agrega una ruta dirigida desde 'origen' hacia 'destino' con su peso.
        Si los nodos aún no existen, se agregan automáticamente.
        
        Parámetros:
            origen (int): ID de la sucursal de salida.
            destino (int): ID de la sucursal de llegada.
            peso (int/float): distancia o costo de la ruta.
        """
         # Asegurar que existan los nodos
        while origen >= len(self.adyacencias):
            self.agregar_sucursal()
        while destino >= len(self.adyacencias):
            self.agregar_sucursal()
#Después, cuando agrego rutas, agrego tuplas dentro de esa sublista, indicando hacia dónde va y la distancia
        self.adyacencias[origen].append((destino, peso))


    def obtener_vecinos(self, nodo):
        """
        Devuelve la lista de vecinos (destino, peso) de un nodo dado.
        
        Parámetros:
            nodo (int): ID de la sucursal.
        
        Retorna:
            list: lista de tuplas (vecino, peso)
        """
        return self.adyacencias[nodo]

    
    