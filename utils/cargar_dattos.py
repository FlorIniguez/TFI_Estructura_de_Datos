from modelos.paquete import Paquete
from modelos.sucursal import Sucursal
from estructuras.arbol_binario_busqueda import ArbolBinarioBusqueda
from estructuras.heap_prioridad import MinHeap
from estructuras.grafo_sucursales import Grafo

def cargar_datos_iniciales():

    # ============================================================
    # 1) Crear grafo y nodos de sucursales
    
    grafo = Grafo()

    # Creo e inserto 10 nodos (IDs 0 a 9)
    for _ in range(10):
        grafo.agregar_sucursal()


    # ============================================================
    # 2) Crear instancias de Sucursales (datos descriptivos)
   
    sucursales = [
        Sucursal(0, "Buenos Aires", "CABA"),
        Sucursal(1, "La Plata", "BA"),
        Sucursal(2, "Mar del Plata", "BA"),
        Sucursal(3, "Rosario", "Santa Fe"),
        Sucursal(4, "Córdoba", "Córdoba"),
        Sucursal(5, "Mendoza", "Mendoza"),
        Sucursal(6, "San Luis", "San Luis"),
        Sucursal(7, "Neuquén", "Neuquén"),
        Sucursal(8, "Bariloche", "Río Negro"),
        Sucursal(9, "Ushuaia", "Tierra del Fuego"),
    ]

    # Diccionario para buscar  Id de sucursales por nombre
    #s.nombre.lower(): s.id_sucursal Transformo cada nombre e id de sucursal en un diccionario
    #Luego con el for recorro toda la lista de sucursales para guardarlas
    mapa_sucursales = {s.nombre.lower(): s.id_sucursal for s in sucursales}


    # ============================================================
    # 3) Agregar rutas entre sucursales (grafo dirigido)
    #Conecto los nodos del grafo
    grafo.agregar_ruta(0, 1, 60)      # BA → La Plata
    grafo.agregar_ruta(1, 2, 350)     # La Plata → Mar del Plata

    grafo.agregar_ruta(0, 3, 300)     # BA → Rosario
    grafo.agregar_ruta(3, 4, 400)     # Rosario → Córdoba
    grafo.agregar_ruta(4, 5, 650)     # Córdoba → Mendoza
    grafo.agregar_ruta(4, 6, 250)     # Córdoba → San Luis

    grafo.agregar_ruta(5, 7, 1000)    # Mendoza → Neuquén
    grafo.agregar_ruta(7, 8, 450)     # Neuquén → Bariloche
    grafo.agregar_ruta(8, 9, 1500)    # Bariloche → Ushuaia


    # ============================================================
    # 4) Crear lista de Paquetes

    paquetes = [
        Paquete(101, 5, 1, "Buenos Aires", "Ushuaia"),
        Paquete(102, 10, 3, "La Plata", "Córdoba"),
        Paquete(103, 4, 2, "Mar del Plata", "Mendoza"),
        Paquete(104, 2, 1, "Buenos Aires", "Bariloche"),
        Paquete(105, 7, 2, "Rosario", "San Luis"),
        Paquete(106, 3, 3, "Córdoba", "Neuquén"),
        Paquete(107, 6, 1, "Mendoza", "Ushuaia"),
        Paquete(108, 8, 2, "Bariloche", "Mar del Plata"),
    ]

    # ============================================================
    # 5) Historial de un paquete (ejemplo)

    #"agarro" el primer paquete de la lista, lo asigno a la variable p1
    p1 = paquetes[0]

    h1 = p1.historial.agregar_hijo(p1.historial.raiz, "Creado")
    h2 = p1.historial.agregar_hijo(p1.historial.raiz, "Clasificado en BA")

    p1.historial.agregar_hijo(h2, "En tránsito a Rosario")
    p1.historial.agregar_hijo(p1.historial.raiz, "Entregado")
    
    p2 = paquetes[1]
    h1 = p2.historial.agregar_hijo(p1.historial.raiz, "Creado")
    h2 = p2.historial.agregar_hijo(p1.historial.raiz, "Ingresado en sucursal en BA")
    p2.historial.agregar_hijo(h2, "Clasificado en BA")
    p2.historial.agregar_hijo(h2, "Esperando retiro")
    

  
    # =================================================================
    # 6) Cargar paquetes en ABB

    abb = ArbolBinarioBusqueda()
    for paquete in paquetes:
        abb.insertar(paquete)

    # ============================================================
    # 7) Cargar paquetes en Heap de prioridades

    heap = MinHeap()
    for paquete in paquetes:
        heap.insertar_paquete(paquete)

    ultimo_id = max(p.id_paquete for p in paquetes)


    # ============================================================
    # 8) Retornar estructuras

    return grafo, sucursales, paquetes, abb, heap, mapa_sucursales, ultimo_id

