class NodoABB:
    def __init__(self,paquete):
        self.paquete = paquete
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    """
    Implementa un Árbol Binario de Búsqueda (ABB) para almacenar paquetes
    ordenados por su ID. Permite inserción, búsqueda y recorrido
    inorder para mostrar los elementos ordenados.

    El ABB es ideal para búsqueda rápida por ID.
    """
    def __init__(self):
        self.raiz = None
        
    #Insertar paquete    
    def insertar(self,paquete):
        """
        Inserta un paquete en el ABB respetando el orden por ID.

        Parámetros:
            paquete (Paquete): objeto a insertar.
        """
        if self.raiz is None:
            self.raiz = NodoABB(paquete)
        else:
            self._insertar_rec(self.raiz,paquete)
            
    #Funcion recuersiva,ubica el paquete en su lugar    
    def _insertar_rec(self,nodo,paquete):
        """
        Inserción recursiva en el subárbol correspondiente.
        Regresa:
            NodoABB: nodo actualizado.
        """
        if nodo is None:
            return NodoABB(paquete)
        if paquete.id_paquete < nodo.paquete.id_paquete:
            nodo.izq = self._insertar_rec(nodo.izq,paquete)
        else:
            nodo.der = self._insertar_rec(nodo.der,paquete)
        return nodo  
      
    # Buscar paquete por ID
    def buscar_paquete_id(self, id_paquete):
        """
        Busca un paquete en el ABB utilizando su ID.

        Retorna:
            Paquete si existe, o None si no se encuentra.
        """
        return self._buscar_rec(self.raiz, id_paquete)
    
    def _buscar_rec(self,nodo,id_paquete):
        if nodo is None:
            return None
        
        if id_paquete == nodo.paquete.id_paquete:
            return nodo.paquete
        
        if id_paquete < nodo.paquete.id_paquete:
            return self._buscar_rec(nodo.izq, id_paquete)
        else:
            return self._buscar_rec(nodo.der, id_paquete)
        
    #Mostrar paquetes, RECORRIDO INORDEN
    def inorden(self):
        """Muestra los paquetes ordenados por ID usando recorrido inorder."""
        self._inorden_rec(self.raiz)
    
    def _inorden_rec(self,nodo):
        if nodo:
            self._inorden_rec(nodo.izq)
            print(nodo.paquete)
            self._inorden_rec(nodo.der)
            
    
            
    