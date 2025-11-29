import heapq

def dijkstra(grafo, origen, destino):
    """
    Calcula el camino más corto entre 'origen' y 'destino' en un grafo ponderado,
    utilizando el algoritmo de Dijkstra.

    Retorna:
        (distancia_minima, camino):
            distancia_minima -> costo total del camino más corto (cantidad de kms)
            camino -> lista con los nodos que conforman el camino (nodos visitados para llegar)
        Si no existe camino, retorna (None, None).
    """
    # Inicializo las distancias en infinito
    dist = [float('inf')] * len(grafo.adyacencias)
    dist[origen] = 0  # La distancia al origen es 0

    # Vector para reconstruir el camino
    padre = [-1] * len(grafo.adyacencias)
    # Cola de prioridad con tuplas (distancia_acumulada, nodo)
    heap = [(0, origen)]  

    while heap:
        # Extraemos el nodo con la menor distancia acumulada
        d_actual, nodo = heapq.heappop(heap)

        # Si el nodo que sacamos tiene distancia mayor a la registrada, lo ignoramos
        if d_actual > dist[nodo]:
            continue

        # Si llegamos al destino, podemos cortar (optimización)
        if nodo == destino:
            break

        # Recorremos los vecinos
        for vecino, peso in grafo.obtener_vecinos(nodo):
            # Costo de ir al vecino pasando por 'nodo'
            nueva = d_actual + peso

            # Si encontramos un camino más corto hacia "vecino", lo actualizamos
            if nueva < dist[vecino]:
                dist[vecino] = nueva
                padre[vecino] = nodo
                heapq.heappush(heap, (nueva, vecino))

    # Si el destino quedó en inf, no hay camino
    if dist[destino] == float('inf'):
        return None, None

    # RECONSTRUIR EL CAMINO usando el vector padre
    camino = []
    nodo = destino
    while nodo != -1:
        camino.append(nodo)
        nodo = padre[nodo]

    camino.reverse()

    return dist[destino], camino

def dijkstra_mostrar(grafo, sucursales,origen_id, destino_id):
    # Validación de IDs
    n_sucursales = len(sucursales)
    if origen_id < 0 or origen_id >= n_sucursales or destino_id < 0 or destino_id >= n_sucursales:
        print("Alguna sucursal no existe.")
        return

    distancia, camino = dijkstra(grafo, origen_id, destino_id)

    if distancia is None:
        print("No existe camino entre esas sucursales.")
        return

    # Convertimos IDs a nombres para mostrar al usuario
    nombres = [sucursales[n].nombre for n in camino]

    print("\n--- Resultado Dijkstra ---")
    print("Camino más corto:", " → ".join(nombres))
    print("Distancia total:", distancia, "km")
