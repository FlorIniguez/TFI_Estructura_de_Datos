class MinHeap:
    def __init__(self):
        """Heap mínimo representado con una lista (árbol binario completo)."""
        self.datos = []

    # ------------------ ÍNDICES ------------------
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
        El heap comparará automáticamente por prioridad.
        """
        tupla = (paquete.prioridad, paquete)
        self.insertar(tupla)

    # ------------------ INSERTAR ELEMENTO ------------------
    def insertar(self, valor):
        """
        Inserta una tupla (prioridad, paquete) en el heap
        y aplica 'flotar hacia arriba' para mantener el Min-Heap.
        """
        self.datos.append(valor)
        i = len(self.datos) - 1

        # Mientras el elemento tenga mayor prioridad que su padre, se intercambia
        while i > 0 and self.datos[i][0] < self.datos[self.padre(i)][0]:
            self.datos[i], self.datos[self.padre(i)] = self.datos[self.padre(i)], self.datos[i]
            i = self.padre(i)

    # ------------------ PROCESAR (SACAR MÍNIMO) ------------------
    def procesar(self):
        """
        Elimina y devuelve el paquete de mayor prioridad (prioridad más baja numéricamente).
        Retorna SOLO el paquete, no la tupla.
        """
        if self.esta_vacio():
            return None

        prioridad, paquete = self.eliminar_min()
        return paquete

    # ------------------ ELIMINAR MÍNIMO ------------------
    def eliminar_min(self):
        """
        Elimina la raíz del heap (tupla de menor prioridad) y reordena el heap
        aplicando 'heapify-down'.

        Retorna:
            (prioridad, paquete)
        """
        if not self.datos:
            return None

        if len(self.datos) == 1:
            return self.datos.pop()

        minimo = self.datos[0]
        self.datos[0] = self.datos.pop()
        self._heapify_down(0)

        return minimo

    # ------------------ HEAPIFY DOWN ------------------
    def _heapify_down(self, i):
        menor = i
        izq = self.hijo_izq(i)
        der = self.hijo_der(i)

        # Comparar con hijo izquierdo
        if izq < len(self.datos) and self.datos[izq][0] < self.datos[menor][0]:
            menor = izq

        # Comparar con hijo derecho
        if der < len(self.datos) and self.datos[der][0] < self.datos[menor][0]:
            menor = der

        # Si uno de los hijos es menor, intercambiar
        if menor != i:
            self.datos[i], self.datos[menor] = self.datos[menor], self.datos[i]
            self._heapify_down(menor)

    # ------------------ VERIFICAR VACÍO ------------------
    def esta_vacio(self):
        """Retorna True si el heap no contiene elementos."""
        return len(self.datos) == 0
