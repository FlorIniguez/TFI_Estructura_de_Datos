from collections import deque

def orden_topologico(grafo):
    """
    Ordenamiento topológico sobre un grafo dirigido utilizando 
    el algoritmo de Kahn.
    Este tipo de ordenamiento solo es posible si el grafo NO contiene ciclos 

    ---------- Retorna ----------
    list[int] | None
        - Una lista con los nodos en orden topológico si el grafo no tiene ciclos.
        - None si el grafo contiene ciclos y el ordenamiento no es posible.
    """
    #n cantidad de nodos del grafo
    n = len(grafo.adyacencias)
    #Grado de entrada cuantas aristas entran al nodo i 
    grado_entrada = [0] * n

    # Calcular grados de entrada (IMPORTANTE en grafos dirigidos)
    #Se recorren las aristas u -> v del nodo v, recibe un aumento en su grado de entrada
    for u in range(n):
        for v, _ in grafo.obtener_vecinos(u):
            grado_entrada[v] += 1
    #Creo cola con los nodos sin dependencias
    cola = deque([i for i in range(n) if grado_entrada[i] == 0])
    #Se agregan a la cola todos los nodos que no tienen aristas entrando.
    #Es el punto de inicio del orden topológico.
    
    orden = []

    while cola:
        #Se extrae un nodo sin dependencias y se agrega al orden final.
        u = cola.popleft()
        orden.append(u)

        for v, _ in grafo.obtener_vecinos(u):
            #Bajo grado de entrada de sus vecinos, cuando elimimo un nodo
            grado_entrada[v] -= 1
            if grado_entrada[v] == 0:
                cola.append(v)

    # Si no visitó todos, hay ciclo
    if len(orden) != n:
        return None

    return orden

def mostrar_orden_topologico(grafo, sucursales):
    orden = orden_topologico(grafo)

    if orden is None:
        print("El grafo contiene ciclos. No es posible ordenarlo.")
        return

    nombres = [sucursales[n].nombre for n in orden]
    print("Orden topológico:", " → ".join(nombres))
