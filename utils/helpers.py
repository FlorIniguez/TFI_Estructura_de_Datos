from modelos.sucursal import Sucursal

#   AGREGAR SUCURSAL
def agregar_sucursal(sucursales, grafo, mapa_sucursales):
    print("\n--- Agregar Nueva Sucursal ---")
    
    nombre = input("Nombre: ")
    prov = input("Provincia: ")
    dirr = input("Dirección: ")

    # El ID de la nueva sucursal será la posición en la lista
    nuevo_id = len(sucursales)

    nueva = Sucursal(nuevo_id, nombre, prov, dirr)

    # Agregar a la lista
    sucursales.append(nueva)

    # Agregar nodo al grafo (una nueva lista vacía de adyacencias)
    grafo.adyacencias.append([])

    # Agregar al mapa de nombres
    mapa_sucursales[nombre.lower()] = nuevo_id

    print("\nSucursal agregada correctamente.\n")


#   MODIFICAR SUCURSAL
def modificar_sucursal(sucursales, mapa_sucursales):
    print("\n--- Modificar Sucursal ---")
    nombre = input("Nombre actual de la sucursal: ").lower()

    if nombre not in mapa_sucursales:
        print("La sucursal no existe.")
        return

    idx = mapa_sucursales[nombre]
    suc = sucursales[idx]

    print(f"\nModificando: {suc.nombre}")
    print("eNTER para mantener el valor actual.\n")

    nuevo_nombre = input(f"Nuevo nombre ({suc.nombre}): ").strip()
    nueva_prov = input(f"Nueva provincia ({suc.provincia}): ").strip()
    nueva_dir = input(f"Nueva dirección ({suc.direccion}): ").strip()

    # CAMBIO DE NOMBRE (hay que actualizar el diccionario)
    if nuevo_nombre:
        del mapa_sucursales[nombre]              # Borro el viejo nombre
        suc.nombre = nuevo_nombre                # Actualizo la sucursal
        mapa_sucursales[nuevo_nombre.lower()] = idx  # Registro nuevo

    if nueva_prov:
        suc.provincia = nueva_prov
    
    if nueva_dir:
        suc.direccion = nueva_dir

    print("\nSucursal modificada correctamente.\n")
# < num alineo a la izquierda y ocupa num cantidad de caracteres, si tiene menos deja el espacio
def listar_sucursales(sucursales):
    print("\n--- Lista de Sucursales ---")
    print(f"{'ID':<3} | {'Nombre':<15} | {'Provincia':<15} | {'Dirección'}")
    print("-" * 60)
    for s in sucursales:
        print(f"{s.id_sucursal:<3} | {s.nombre:<15} | {s.provincia:<15} | {s.direccion}")
