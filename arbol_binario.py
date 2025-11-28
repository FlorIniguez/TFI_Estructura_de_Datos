from collections import deque
class Nodo_Arbol:
    def __init__(self,dato):
        self.dato = dato
        self.der = None
        self.izq = None
        
    #Creo clase nodo, le asigno el dato e inicializo los hijos como None

class Arbol_binario:
    def __init__(self):
        self.raiz = None
    #Creo clase arbol con su raiz como None
    
    def insertar_nodo(self,dato):
        #Si la raiz esta vacia, creo un nodo con ese dato y lo asigno como raiz
        if self.raiz is None:
            self.raiz = Nodo_Arbol(dato)
        #Sino llamo insetar recursivo
        else:
            self._insertar_rec(self.raiz,dato)
            
    def _insertar_rec(self,nodo,dato):
        #Recibo el nodo raiz y el dato a insertar
        if nodo is None:
            return Nodo_Arbol(dato)
        #Si el dato a insertar es menor al valor del nodo raiz, me voy del lado izq
        if dato < nodo.dato:
            nodo.izq = self._insertar_rec(nodo.izq,dato)
        else:
            nodo.der = self._insertar_rec(nodo.der,dato)
        return nodo
    
    # -------- Recorrido de arboles binarios ---------
    
    #INORDEN (IZQ, RAIZ DERECHA)
    def inorden(self):
        self._inorden_rec(self.raiz)
    #Baja hasta el ultimo nodo izq y de ahi sube,     
    def _inorden_rec(self,nodo):
        if nodo is not None:
            self._inorden_rec(nodo.izq) 
            print(nodo.dato)
            self._inorden_rec(nodo.der)
    
    def inorden_pares(self):
        return self._inorden_rec_pares(self.raiz)
            
    def _inorden_rec_pares(self,nodo):
        if nodo is None:
            return 0
        # contar pares en subárbol izquierdo
        pares_izq = self._inorden_rec_pares(nodo.izq)
    
        # contar el nodo actual
        pares_actual = 1 if nodo.dato % 2 == 0 else 0
    
        # contar pares en subárbol derecho
        pares_der = self._inorden_rec_pares(nodo.der)
    
        # devolver el total
        return pares_izq + pares_actual + pares_der
        
    # PREORDEN (RAIZ, IZQ, DER)
    def preorden(self):
        self._preorden_rec(self.raiz)
    # Imprime raiz y va bajando   
    def _preorden_rec(self,nodo):
        if nodo is not None:
            print(nodo.dato)
            self._preorden_rec(nodo.izq)
            self._preorden_rec(nodo.der)
            
    # Multiplos de 3
    def _imprimir_multiplos_3_inorden_rec(self, nodo):
        if nodo is None:
            return
        # subárbol izquierdo
        self._imprimir_multiplos_3_inorden_rec(nodo.izq)
        # nodo actual
        if nodo.dato % 3 == 0:
            print(nodo.dato, end=' ')
        # subárbol derecho
        self._imprimir_multiplos_3_inorden_rec(nodo.der)

    
    def contar_mul3(self):
        return self._multiplos_3_preorden_rec(self.raiz)
        
            
    #POST ORDEN (DER,IZQ,RAIZ)
    def posorden(self):
        self._posorden_rec(self.raiz)
        
    def _posorden_rec(self,nodo):
        if nodo is not None:
            self._posorden_rec(nodo.izq)
            self._posorden_rec(nodo.der)
            print(nodo.dato)
            
    def contar_pares(self):
        return self._contar_pares_rec(self.raiz)

    def _contar_pares_rec(self, nodo):
        if nodo is None:
            return 0
        # verifico si el valor es par
        if nodo.dato % 2 == 0:
            cuenta = 1 
        else:
            
            0
        # sigo recorriendo izquierda y derecha
        cuenta += self._contar_pares_rec(nodo.izq)
        cuenta += self._contar_pares_rec(nodo.der)
        return cuenta
           
    def recorrer_niveles(self):
        if self.raiz is None:
            return
        
        cola = deque()
        cola.append(self.raiz)
        
        while cola:
            nodo = cola.popleft()  # sacar el primer nodo de la cola
            print(nodo.dato)      # visitar el nodo
            
            if nodo.izq is not None:
                cola.append(nodo.izq)  # agregar hijo izquierdo
            if nodo.der is not None:
                cola.append(nodo.der)  # agregar hijo derecho
                
    # pares inorden
    def contar_pares(self):
        return self._contar_pares_inorden_rec(self.raiz)
    
    def _contar_pares_inorden_rec(self,nodo):
        if nodo is None:
            return 0
        #Como es el primero va =
        cuenta = self._contar_pares_inorden_rec(nodo.izq)
        if nodo.dato % 2 ==0:
            cuenta += 1
       
        cuenta += self._contar_pares_inorden_rec(nodo.der)
        return cuenta
    
    def pares_postorden(self):
        return self._contar_postorden_rec(self.raiz)
    
    def _contar_postorden_rec(self,nodo):
        if nodo is None:
            return 0
        #Como es el primero va =
        cuenta = self._contar_postorden_rec(nodo.izq)
        cuenta += self._contar_postorden_rec(nodo.der)
        if nodo.dato % 2 ==0:
            cuenta +=1
        return cuenta
        
        
    
arbol = Arbol_binario()
arbol.insertar_nodo(50)
arbol.insertar_nodo(30)
arbol.insertar_nodo(70)
arbol.insertar_nodo(20)
arbol.insertar_nodo(40)
arbol.insertar_nodo(60)
arbol.insertar_nodo(80)

print("Inorden:")
arbol.inorden()

print("\nPreorden:")
arbol.preorden()

print("\nPostorden:")
arbol.posorden()

print("\nPor niveles:")
arbol.recorrer_niveles()

print("Cantidad de pares:", arbol.inorden_pares())
print("Cantidad de pares:", arbol.contar_pares())
print("Cantidad de pares:", arbol.pares_postorden())
            
    
   
    
            
        
    