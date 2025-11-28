from modelos.paquete import Paquete
from modelos.sucursal import Sucursal
from algoritmos.dfs_bfs import dfs_camino, bfs_camino
from algoritmos.dijkstra import dijkstra
from algoritmos.topologico import orden_topologico
from utils.cargar_dattos import cargar_datos_iniciales
from utils.registrar_paquete import registrar_paquete
"""
Árbol General → historial de paquetes

ABB → búsqueda rápida por ID de paquete

Heap de prioridad (MinHeap) → procesar primero envíos urgentes

Grafo dirigido → rutas entre sucursales

BFS/DFS → caminos (bfs mas corto y dfs algun camino)

Dijkstra → camino más corto con pesos

Topológico → dependencias de rutas / detectar ciclos en la red

"""

# CARGA DE DATOS (grafo, sucursales, paquetes, abb, heap)

grafo,sucursales, paquetes,abb, heap, mapa_sucursales, ultimo_id = cargar_datos_iniciales()

# ==============================
# FUNCIÓN PARA BUSCAR PAQUETE

def buscar_paquete_en_abb(abb, id_paquete):
    nodo = abb.raiz
    while nodo is not None:
        if id_paquete == nodo.paquete.id_paquete:
            return nodo.paquete
        elif id_paquete < nodo.paquete.id_paquete:
            nodo = nodo.izq
        else:
            nodo = nodo.der
    return None
"""
Sistema de Gestión de Envíos - Datos precargados para pruebas

Sucursales (ID → Nombre):
-------------------------
0 → Buenos Aires (CABA)
1 → La Plata (BA)
2 → Mar del Plata (BA)
3 → Rosario (Santa Fe)
4 → Córdoba (Córdoba)
5 → Mendoza (Mendoza)
6 → San Luis (San Luis)
7 → Neuquén (Neuquén)
8 → Bariloche (Río Negro)
9 → Ushuaia (Tierra del Fuego)

Paquetes precargados:
---------------------
ID | Peso | Prioridad | Origen        | Destino
101 |   5  |     1     | Buenos Aires  | Ushuaia
102 |  10  |     3     | La Plata      | Córdoba
103 |   4  |     2     | Mar del Plata | Mendoza
104 |   2  |     1     | Buenos Aires  | Bariloche
105 |   7  |     2     | Rosario       | San Luis
106 |   3  |     3     | Córdoba       | Neuquén
107 |   6  |     1     | Mendoza       | Ushuaia
108 |   8  |     2     | Bariloche     | Mar del Plata

  ------- Paquetes con historial cargado ID 101 y 102 ---------
"""
def menu():
    global ultimo_id   # ← NECESARIO para modificar la variable de afuera8
    while True:
        print("\n====================================")
        print("     SISTEMA DE ENVÍOS - MENÚ       ")
        print("====================================")
        print("1. Mostrar paquetes en ABB (inorden)")
        print("2. Procesar paquetes por prioridad (Heap)")
        print("3. Ver historial de un paquete (arbol general)")
        print("4. Camino más corto (BFS)")
        print("5. Camino posible (DFS)")
        print("6. Camino mínimo por distancia (Dijkstra)")
        print("7. Ordenamiento Topológico")
        print("8. Ingresar nuevo paquete")
        print("0. Salir")
        
        opcion = input("\nElegí una opción: ")

 
        if opcion == "1":
            print("\n--- Paquetes en ABB (inorden) ---")
            abb.inorden()
   
        elif opcion == "2":
            print("\n--- Procesando paquetes (Heap) ---")
            if heap.esta_vacio():
                print("No hay paquetes para procesar.")
            else:
                while not heap.esta_vacio():
                    print(heap.procesar())

        elif opcion == "3":
            print("\n--- Ver historial ---")
            pid = int(input("ID del paquete: "))

            paquete = abb.buscar_paquete_id(pid)
            if paquete is None:
                print("Paquete no encontrado en el ABB.")
            else:
                print(f"Historial del paquete {pid}:")
                paquete.historial.mostrar(paquete.historial.raiz)

        elif opcion == "4":
            print("\n--- BFS Camino más corto (en tramos) ---")

            o = int(input("ID Sucursal origen: "))
            d = int(input("ID Sucursal destino: "))

            if o >= len(sucursales) or d >= len(sucursales):
                print("Alguna sucursal no existe.")
                continue

            camino = bfs_camino(grafo, o, d)

            if camino is None:
                print("No existe camino entre las sucursales.")
            else:
                nombres = [sucursales[n].nombre for n in camino]
                print("Camino:", " → ".join(nombres))


        elif opcion == "5":
            print("\n--- DFS Algún camino posible ---")

            o = int(input("ID Sucursal origen: "))
            d = int(input("ID Sucursal destino: "))

            if o >= len(sucursales) or d >= len(sucursales):
                print("Alguna sucursal no existe.")
                continue

            camino = dfs_camino(grafo, o, d)

            if camino is None:
                print("No existe ruta posible.")
            else:
                nombres = [sucursales[n].nombre for n in camino]
                print("Camino:", " → ".join(nombres))

        elif opcion == "6":
            print("\n--- Dijkstra ---")
            print("Ingrese el NOMBRE de la sucursal (ej: 'Buenos Aires', 'Bariloche', 'Ushuaia')")

            origen_nombre = input("Sucursal origen: ").lower()
            destino_nombre = input("Sucursal destino: ").lower()

            if origen_nombre not in mapa_sucursales or destino_nombre not in mapa_sucursales:
                print("Alguna sucursal no existe.")
                continue

            o = mapa_sucursales[origen_nombre]
            d = mapa_sucursales[destino_nombre]

            distancia, camino = dijkstra(grafo, o, d)

            if distancia is None:
                print("No existe camino entre esas sucursales.")
            else:
                nombres = [sucursales[n].nombre for n in camino]
                print("Camino más corto:", " → ".join(nombres))
                print("Distancia total:", distancia, "km")

  
        elif opcion == "7":
            print("\n--- Orden Topológico ---")

            orden = orden_topologico(grafo)

            if orden is None:
                print("El grafo contiene ciclos. No es posible ordenarlo.")
            else:
                nombres = [sucursales[n].nombre for n in orden]
                print("Orden:", " → ".join(nombres))
                
        elif opcion == "8":
            ultimo_id = registrar_paquete(abb, heap, paquetes, mapa_sucursales, ultimo_id)


        elif opcion == "0":
            print("Saliendo...")
            break
        
        else:
            print("Opción incorrecta.")

menu()