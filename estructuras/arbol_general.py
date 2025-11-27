#   -------  HISTORIAL DEL PAQUETE ---------- 

class NodoGeneral:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []


class ArbolGeneral:
    """
    Representa el historial de un paquete utilizando un Árbol General.
    Cada nodo corresponde a un estado del envío y puede tener múltiples subestados (creado, en sucursal orginen, clasificado,
    en transito a una sucursal, entregado,etc ).
    El recorrido del árbol se realiza mediante DFS, mostrando la jerarquía del historial.
    """
    def __init__(self, dato_raiz):
        self.raiz = NodoGeneral(dato_raiz)

    def agregar_hijo(self, nodo_padre, dato):
        """Agrega un nuevo estado (hijo) al nodo padre."""
        nuevo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo)
        return nuevo

    def buscar_nodo(self, nodo, dato):
        """Búsqueda recursiva de un estado dentro del historial."""
        if nodo.dato == dato:
            return nodo

        for hijo in nodo.hijos:
            encontrado = self.buscar_nodo(hijo, dato)
            if encontrado:
                return encontrado
        return None

    def mostrar(self, nodo, nivel=0):
        """Muestra el historial completo con un recorrido DFS."""
        print("   " * nivel + "- " + nodo.dato)

        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)
