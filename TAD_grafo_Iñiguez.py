from collections import deque
class Grafo:
    def __init__(self):
        #Diccionario donde voy a guardar vertice como clave
        #Cada valor es una lista de adyacentes, donde cada elemento es una lista del destino y peso
        self.adyacencia = {}
    
    """
    self.adyacencia = {
    "A": [["B", 5], ["C", 3]],
    "B": [["C", 2]],
    "C": [["A", 4]]
}

    """
    def agregar_vertice(self,vertice):
        #Si no existe lo agrego con una lista vacia de adyacencia
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []
    
    def agregar_arista(self,origen,destino,peso):
        #Me fijo que existan los verties, sino los agrega
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        #Creo la conexion dirigida con su peso
        self.adyacencia[origen].append([destino,peso])
        
    def mostrar(self):
        print("Grafo dirigido con peso: ")
        for origen in self.adyacencia:
            for destino,peso in self.adyacencia[origen]:
                print(f"{origen} -> {destino} (peso: {peso})")

    # BUSQUEDAS
    
    # DFS busqueda de profundidad
    #vamos por un camino hasta el final antes de retroceder. 
    #Me muesra si existe el camino, si hay conectividad, detectar ciclos
    def dfs(self,inicio,visitados = None):
    #Inicio va a ser el nodo donde empiezo
    #Visitados un conj donde guardo los nodos que ya vi. Conj para no repetir
        if visitados is None:
            visitados = set()
        #Marco el nodo actual como visitado
        visitados.add(inicio)
        print(inicio, end=" ")
        #Recorro los nodos a los que esta conectado el nodo actual
        # el _ es porque la arista tiene peso, pero como no lo usamos, lo ignoramos
        for vecino, _ in self.adyacencia[inicio]:
            if vecino not in visitados:
                #Si el vecino no fue visitado llamo de nuevo a dfs
                self.dfs(vecino,visitados)
                
    # DFS ITERATIVO CON PILA
    """ 
    def dfs_iterativo(self, inicio):
        visitados = set()
        pila = [inicio]

        while pila:
            nodo = pila.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                print(nodo, end=" ")
                for vecino, _ in self.adyacencia[nodo]:
                    if vecino not in visitados:
                        pila.append(vecino)            
    """            
                
     #BFS busqueda de anchura           
    #explora todos los vecinos a la misma “profundidad” antes de avanzar (cola).
    def bfs(self, inicio):
        #Nodos que ya visite
        visitados = set() 
        #Deque como cola. iniciamos la cola con el nodo de partida.
        cola = deque([inicio])
        visitados.add(inicio)
        #Mientras haya nodos por visitar
        while cola:
            #mientras haya nodos, voy sacando el primero
            nodo = cola.popleft()
            print(nodo, end=" ")
            #Reviso los vecinos
            for vecino, _ in self.adyacencia[nodo]:
                #Si no esta en los que vi, lo agrego a la cola y lo marco como visitado
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        
    
grafo = Grafo()
grafo.agregar_arista("A", "B", 5)
grafo.agregar_arista("A", "C", 3)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("C", "A", 4)
grafo.agregar_arista("C", "D", 7)

grafo.mostrar()

print("Recorrido DFS desde A:")
grafo.dfs("A")

print("\nRecorrido DFS desde C:")
grafo.dfs("C")

print("\nRecorrido BFS desde A:")
grafo.bfs("A")

print("\nRecorrido BFS desde B:")
grafo.bfs("B")
