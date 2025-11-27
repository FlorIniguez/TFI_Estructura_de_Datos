from modelos.paquete import Paquete

def registrar_paquete(abb, heap, paquetes, mapa_sucursales, ultimo_id):
    """
    Registra un nuevo paquete en el sistema:
    - Genera un ID nuevo automáticamente
    - Valida sucursales de origen/destino
    - Crea historial inicial
    - Inserta en ABB, Heap y lista de paquetes
    """
    try:
        origen = input("Sucursal origen: ").lower()
        destino = input("Sucursal destino: ").lower()

        if origen not in mapa_sucursales or destino not in mapa_sucursales:
            print("Error: alguna sucursal no existe.")
            return ultimo_id

        peso = float(input("Peso del paquete (kg): "))
        prioridad = int(input("Prioridad (1 urgente, 2 normal, 3 baja): "))

        # Generar ID automático
        nuevo_id = ultimo_id + 1

        p = Paquete(nuevo_id, peso, prioridad, origen, destino)

        # Historial inicial
        p.historial.agregar_hijo(p.historial.raiz, "Creado")

        # Guardar en estructuras 
        paquetes.append(p)
        abb.insertar(p)
        heap.insertar_paquete(p)

        print(f"Paquete registrado con ID {nuevo_id}")

        return nuevo_id

    except Exception as e:
        print("Error al registrar paquete:", e)
        return ultimo_id
