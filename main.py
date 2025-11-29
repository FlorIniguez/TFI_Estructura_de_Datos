from algoritmos.dfs_bfs import dfs_mostrar_camino, bfs_mostrar_camino
from algoritmos.dijkstra import dijkstra_mostrar
from algoritmos.topologico import mostrar_orden_topologico
from utils.cargar_dattos import cargar_datos_iniciales
from utils.registrar_paquete import registrar_paquete
from utils.helpers import agregar_sucursal,modificar_sucursal, listar_sucursales
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
    global ultimo_id

    print("\n====================================")
    print("     SISTEMA DE ENVÍOS - MENÚ       ")
    print("====================================")
    print("1. Mostrar paquetes en ABB (inorden)")
    print("2. Procesar paquetes por prioridad (Heap)")
    print("3. Ver historial de un paquete")
    print("4. Camino más corto (BFS)")
    print("5. Camino posible (DFS)")
    print("6. Camino mínimo por distancia (Dijkstra)")
    print("7. Ordenamiento Topológico")
    print("8. Ingresar nuevo paquete")
    print("9. Agregar sucursal")
    print("10. Modificar sucursal")
    print("11. Listar sucursales")

    print("0. Salir")

    opcion = input("\nElegí una opción: ")

    match opcion:
        case "1":
            print("\n--- Paquetes en ABB (inorden) ---")
            abb.inorden()

        case "2":
            print("\n--- Procesando paquetes (Heap) ---")
            print(heap.procesar())    

        case "3":
            print("\n--- Ver historial ---")
            pid = int(input("ID del paquete: "))
            paquete = abb.buscar_paquete_id(pid)
            paquete.historial.mostrar(paquete.historial.raiz)

            
        case "4":
            print("\n--- BFS Camino más corto ---")
            o = int(input("ID Sucursal origen: "))
            d = int(input("ID Sucursal destino: "))
            bfs_mostrar_camino(grafo, sucursales, o, d)

        case "5":
            print("\n--- DFS Algún camino posible ---")
            o = int(input("ID Sucursal origen: "))
            d = int(input("ID Sucursal destino: "))
            dfs_mostrar_camino(grafo, sucursales, o, d)

        case "6":
            print("\n--- Dijkstra ---")
            origen =  int(input("ID Sucursal origen: "))
            destino = int(input("ID Sucursal destino: "))

            dijkstra_mostrar(grafo, sucursales, origen, destino)

        case "7":
            print("\n--- Orden Topológico ---")
            mostrar_orden_topologico(grafo,sucursales)

        case "8":
            ultimo_id = registrar_paquete(abb, heap, paquetes, mapa_sucursales, ultimo_id)
            
        case "9":
            agregar_sucursal(sucursales, grafo, mapa_sucursales)

        case "10":
            modificar_sucursal(sucursales, mapa_sucursales)
        
        case "11":
            listar_sucursales(sucursales)
            
        case "0":
            print("Saliendo...")
            return

        case _:
            print("Opción incorrecta.")
    menu()


menu()