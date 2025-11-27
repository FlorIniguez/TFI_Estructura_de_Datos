class MinHeap:
    """
    Implementa un Min-Heap utilizando una lista como estructura base.
    El heap almacena tuplas (prioridad, paquete), permitiendo procesar 
    primero el paquete más urgente (menor prioridad numérica).
    """
    def __init__(self):
        self.datos = [] # El heap se almacena como lista (árbol binario implícito)
        
    # ------------------ ÍNDICES DE NODOS ------------------
    def padre(self, i):
        return (i - 1) // 2

    def hijo_izq(self, i):
        return 2 * i + 1

    def hijo_der(self, i):
        return 2 * i + 2

    # ------------------ INSERTAR PAQUETE ------------------
    def insertar_paquete(self, paquete):
        """
        Inserta un paquete convirtiéndolo en una tupla (prioridad, paquete).
        Esto permite que el heap compare automáticamente por prioridad.
        """
        prioridad = paquete.prioridad
        tupla = (prioridad, paquete)
        self.insertar(tupla)
   
    def insertar(self, valor):
        """
        Inserta una tupla (prioridad, paquete) en el heap,
        manteniendo la propiedad de min-heap mediante 'flotar hacia arriba'.
        """
        self.datos.append(valor)
        i = len(self.datos) - 1

        # Flotar hacia arriba si rompe la propiedad del heap
        while i > 0 and self.datos[i][0] < self.datos[self.padre(i)][0]:
            self.datos[i], self.datos[self.padre(i)] = self.datos[self.padre(i)], self.datos[i]
            i = self.padre(i)

 
    ## ------------------ PROCESAR / ELIMINAR ------------------ 
    def procesar_elimninar(self):
        """
        Elimina y devuelve únicamente el paquete con mayor prioridad.
        """
        if self.esta_vacio():
            return None
        #Desempaqueto la tupla, la separo en 2 variables para tener el paqeute para retornar
        prioridad, paquete = self.eliminar_min()
        #Devuelvo el paquete no la tupla
        return paquete

    # ELIMINAR MINIMO    
    def eliminar_min(self):
        """
        Elimina la raíz del heap (la tupla con menor prioridad)
        y restaura la propiedad del heap.
        
        Retorna:
            tupla (prioridad, paquete)
        """
        if not self.datos:
            return None
       
        if len(self.datos) == 1:
            return self.datos.pop()

        minimo = self.datos[0]     #guardo el minimo, la raiz, tupla (prioridad, paquete)
        #Remplazo la raiz por el ultimo elemento
        self.datos[0] = self.datos.pop()
        #Recorro hacia abajo para restaurar posiciones, 0 porque esta en la posicion 0
        self._heapify_down(0)
        return minimo

 
   # ------------------ REORDENAR HACIA ABAJO ------------------ 
    def _heapify_down(self, i):
        """
        Restaura la propiedad del min-heap comparando con los hijos
        y bajando el nodo si es necesario.
        """
        menor = i
        izq = self.hijo_izq(i)
        der = self.hijo_der(i)
      
        if izq < len(self.datos) and self.datos[izq][0] < self.datos[menor][0]:
            menor = izq
        if der < len(self.datos) and self.datos[der][0] < self.datos[menor][0]:
            menor = der
        #Miro ambos hijos, queda el menor
         # Si alguno de los hijos es menor que el padre, intercambiamos
        if menor != i:
            #Reasigno valores, los intercambio el indice y el dato
            self.datos[i], self.datos[menor] = self.datos[menor], self.datos[i]
            self._heapify_down(menor)

    def esta_vacio(self):
        return len(self.datos) == 0
