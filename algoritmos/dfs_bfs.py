from collections import deque
"""
BFS encuentra caminos mínimos en grafos NO ponderados.
DFS solo verifica conectividad, no sirve para minimizar distancias.
"""

# BFS — Camino mínimo entre dos nodos
def bfs_camino(grafo, inicio, destino):
    """
    Calcula el camino más corto en cantidad de pasos/tramos entre dos nodos(sucursales)
    utilizando BFS.

    Retorna:
        Lista con el camino desde inicio hasta destino, o None si no existe.
    """
    visitado = [False] * len(grafo.adyacencias)
    #Esta lista guarda de doonde vine, para despues reconstruir el camino
    padre = [-1] * len(grafo.adyacencias)

    cola = deque([inicio])
    visitado[inicio] = True

    while cola:
    #Mientras haya nodos por visitar tomo el primero de la cola y proceso
        actual = cola.popleft()

        if actual == destino:
            break
        #Obtener vecinos de ese nodo (obtener_vecinos()esta en la clase grafo 
        # - ignoro el peso porque bfs busca el camino mas corto en pasos   
        for vecino, _ in grafo.obtener_vecinos(actual):
            if not visitado[vecino]:
                visitado[vecino] = True
                padre[vecino] = actual
                cola.append(vecino)
    #Si nunca llegue a destino no hay camino
    if not visitado[destino]:
        return None
    # reconstruir camino, recorro hacia atras destino -> inicio
    camino = []
    nodo = destino
    while nodo != -1:
        camino.append(nodo)
        nodo = padre[nodo]
    #Doy vuelta la lista inicio -> destino
    return camino[::-1]

def bfs_mostrar_camino(grafo, sucursales, inicio, destino):
    if inicio >= len(sucursales) or destino >= len(sucursales):
        print("Alguna sucursal no existe.")
        return

    camino = bfs_camino(grafo, inicio, destino)

    if camino is None:
        print("No existe camino entre las sucursales.")
        return

    nombres = [sucursales[n].nombre for n in camino]
    print("Camino más corto (por tramos):", " → ".join(nombres))


#DFS — Para verificar si existe un camino (NO mínimo)
def dfs_camino(grafo, inicio, destino, visitado=None):
    """
    Busca un camino cualquiera entre dos nodos usando DFS recursivo.
    NO garantiza camino mínimo.

    Retorna:
        Lista con un camino válido, o None si no existe.
    """
    if visitado is None:
        visitado = [False] * len(grafo.adyacencias)
    visitado[inicio] = True

    if inicio == destino:
        return [inicio]
    #Obtener vecinos esta en la clase grafo
    for vecino, _ in grafo.obtener_vecinos(inicio):
        if not visitado[vecino]:
            #Si el vecino no esta visitado hago dfs recursivo
            resultado = dfs_camino(grafo, vecino, destino, visitado)
            #Si encuentro destino construyo el camino al volver
            if resultado is not None:
                return [inicio] + resultado
    #Si no llegue a destino
    return None

def dfs_mostrar_camino(grafo, sucursales, inicio, destino):
    if inicio >= len(sucursales) or destino >= len(sucursales):
        print("Alguna sucursal no existe.")
        return

    camino = dfs_camino(grafo, inicio, destino)

    if camino is None:
        print("No existe un camino posible entre las sucursales.")
        return

    nombres = [sucursales[n].nombre for n in camino]
    print("Camino encontrado (DFS):", " → ".join(nombres))
