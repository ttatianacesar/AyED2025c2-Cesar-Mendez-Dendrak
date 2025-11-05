class NodoArbol: #guardan la info de cada nodo
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None): #creacion y defino info, izq, derecho los creo vacios
        self.clave = clave # guarda el identificador del nodo dentro del arbol, el dato principal
        self.cargaUtil = valor #gurada contenido asociado a esa clave
        self.hijoIzquierdo = izquierdo  #referencia al nodo q esta a la izquierda, valores menores a la clave actual
        self.hijoDerecho = derecho #guarda una referencia al nodo q esta a la derecha, valor mayor a clave actual
        self.padre = padre #guarda referencia/enlace hacia otro objeto, una conexion no una copia al nodo pradre, o sea el nodo q esta encima de este, p poder subir de un nodo a otro
        self.factorEquilibrio = 0 #agregado #se inicializa en 0, esto indica el desbalance

#metodos de consulta, devuelven info sobre el nodo
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo #si tiene hijo izq lo devuelve, sino None

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self): #devuelve true si este nodo es el hijo izq de SU padre, primero comprueba q exista padre, desp compara
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):#si no tiene padre, es porque es raiz, tira True
        return not self.padre

    def esHoja(self): #true si no tiene hijos ni izq ni derecho
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self): #chequeo de que tenga al menos un hijo, izq o derecho
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self): #q tenga los 2 hijos
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder): #reemplaza el contenido de 1 nodo por los datos de otro (clave, valor,hijos)
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo(): #actualiza los padres de los hijos nuevos asi apuntan p este nodo
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    #las saque de la clase de abajo y las meto aca        
    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre
    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual


class ArbolAVL: #define estructura del arbol, maneja nodos, inserciones y rotaciones, cada nodo guarda fecha y T

    def __init__(self): #lo creo
        self.raiz = None #no tiene raiz
        self.tamano = 0 #ni tamaño

    def longitud(self):
        return self.tamano  #devuelve cant nodos
#formas de pedir cuantos elementos hay
    def __len__(self): #p q la clase se comporte como algo propio de python, lista o cadena
        return self.tamano

    def agregar(self,clave,valor): 
        if self.raiz: 
            self._agregar(clave,valor,self.raiz) #si ya hay raiz, llama a _agregar para buscar posicion correcta
        else: #si no hay raiz, crea el 1er nodo como raiz
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1 #incrementa el tamaño xq agrego algo
#este era el del arbolABB:
    """def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                   nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                   self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                   nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)"""


#el agregar es igual que el ABB, se incluye "actualizar equilibrio", es la version con balanceo
    def _agregar(self,clave,valor,nodoActual): #es el q mete en el arbol, empezando a revisar desde el nodo actual
        if clave < nodoActual.clave: #compara clave con nodo actual p ir a izq o derecha, si el num es menor o mayor
            if nodoActual.tieneHijoIzquierdo(): #si va a la izq se fija si ya hay hijo izquierdo
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo) #si es asi, se vuelve a llamar sobre ese p buscar posicion correcta, o sea sobre ese hijo izq que ya existe
            else: #si no tiene hijo izquierdo, se mete
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual) #crea el nodo y lo conecta comonhijo izquierdo del nodo actual y le dice a ese nuevo que su padre es el nodoactual.
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo) #ahora q se metio algo, hay que balancear
        else: #si en vez de ser menor era mayor, viene p la derecha
            if nodoActual.tieneHijoDerecho(): #ver si lo q miro ya tiene hijo dereco
                    self._agregar(clave,valor,nodoActual.hijoDerecho) #si tiene asi que hace lo mismo desde ese hijo, baja, recursividad
            else: #si no tiene hijo derecho, se mete
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) #crea lo nuevo y lo conecta como hijo derecho del nodo actual, indicando quien es su padre
                    self.actualizarEquilibrio(nodoActual.hijoDerecho) #hay q balancearrrr

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)
#comprueba primero si el nodo actual está lo suficientemente desequilibrado como para requerir el
#  reequilibrio (línea 16). Si ése es el caso, entonces se realiza el reequilibrio y no se requiere hacer
#  ninguna nueva actualización a los padres. Si el nodo actual no requiere reequilibrio entonces se ajusta el factor de equilibrio
#  del padre. Si el factor de equilibrio del padre no es cero, entonces el algoritmo continúa ascendiendo en el árbol, hacia la raíz,
#  llamando recursivamente a actualizarEquilibrio con el padre como parámetro.

#ROTACIONES: agregado: cambian estructura del arbol para reducir la altura de un subarbol

#cuando el subarbol derecho es + alto
    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho #agarra el h. derecho la raiz desequilibrada y hace q ahora sea la nueva raiz
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo # si el q ahora es raiz tenia subhijo izq, ahora sera hijo derecho de la vieja raiz
        if nuevaRaiz.hijoIzquierdo != None: #busca h.i. de la raiz nueva, if existe, si es distinto de none significa que hay un nodo conectado ahi
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz #como existe, al nodo que esta como hijo izq de nueva raiz, cambiale el atributo de padre p q apunte a rotRaiz. #hay q actualizar referencias
        #el hij izq ahora tiene como padre a nueva raiz, actualiza el campo padre del nodo q cambio de lugar
        #solo le da nombre a lo que se explico antes. el h.i de nueva raiz ahora es hijo derecho de la raiz vieja
        nuevaRaiz.padre = rotRaiz.padre #ahora la nueva raiz es el padre, sube, el padre q antes era rotRaiz
        if rotRaiz.esRaiz(): #si la raiz vieja era la raiz principal de todo el arbol, entonces ahora la raiz nueva sera principal, o sea le cambia el puesto.
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo(): #si la raiz vieja no era principal
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz #ahora el padre es la raiz nueva .
                    #hij izq si hay q sust el enlace izq
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz #si hay q sust el enlace derecho
        nuevaRaiz.hijoIzquierdo = rotRaiz #ahora la raiz vieja es hijo izq de la raiz nueva
        rotRaiz.padre = nuevaRaiz #actualizo quien es el padre ahora, la raiz nueva, lo q antes era raiz vieja
        #cada nodo del arbol tiene un fact eq. al rotar cambian esos fe, asi q hay q recalcularlos p mostrar la nueva forma del arbol
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0) #actualiza balance del nodo q bajo, haciendo el calculo con el que acaba de subir en reemplazo de este
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0) #actualiza el balance del q subio, teniendo en cuenta el q ahora tiene abajo

#rotar derecha--> simetrica a rotar izq: #si esta pesado el lado izq, rota a la derecha
    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo #el hijo izq de la raiz vieja ahora es raiz nueva
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho #el q era hijo derecho de la raiz nueva ahora es h izq de la vieja
        if nuevaRaiz.hijoDerecho != None: #si exsiste el hd de la raiz nueva
            nuevaRaiz.hijoDerecho.padre = rotRaiz #el hijo derecho ahora tiene como padre a la raiz nueva
        nuevaRaiz.padre = rotRaiz.padre #actualizo nombre del padre
        if rotRaiz.esRaiz(): #si la vieja era principal
            self.raiz = nuevaRaiz #ahora la q ocupó su lugar sera principal
        else: #si no era principal
            if rotRaiz.esHijoDerecho(): #compruebo q haya sido h.d. de su padre
                rotRaiz.padre.hijoDerecho = nuevaRaiz #ahora la nueva raiz va a ser padre de su h.d
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz #o de su h.izq
        nuevaRaiz.hijoDerecho = rotRaiz #ahora la vieja es hijo derecho de la nueva
        rotRaiz.padre = nuevaRaiz #y la nueva es padre de la vieja

        # actualización de factores de equilibrio (simétrica a rotarIzquierda)
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(rotRaiz.factorEquilibrio, 0)


#REEQUILIBRIO:
    def reequilibrar(self,nodo): 
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def __setitem__(self,c,v):
        self.agregar(c,v)

    def obtener(self,clave):
       if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                  return res.cargaUtil
           else:
                  return None
       else:
           return None

    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.hijoIzquierdo)
       else:
           return self._obtener(clave,nodoActual.hijoDerecho)

    def __getitem__(self,clave):
       return self.obtener(clave)

    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False

    #CAMBIO ELIMINAR, ahora llama a remover
    def eliminar(self, clave):
        """Busca el nodo con la clave y lo elimina usando remover"""
        if self.tamano > 1:
            nodo_a_eliminar = self._obtener(clave, self.raiz)
            if nodo_a_eliminar:
                self.remover(nodo_a_eliminar)
                self.tamano -= 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano -= 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
        self.reequilibrar(self.raiz)


    
#CAMBIO MI REMOVER: asi llama a actualizar equilibrio despues de eliminar
    def remover(self, nodo_actual, usar_predecesor=False):
        """Elimina un nodo una vez encontrado"""
        # Nodo hoja
        if nodo_actual.esHoja():
            if nodo_actual.esHijoIzquierdo():
                nodo_actual.padre.hijoIzquierdo = None
            else:
                nodo_actual.padre.hijoDerecho = None

        # Nodo con ambos hijos
        elif nodo_actual.tieneAmbosHijos():
            # Elegir sucesor  # no usar predecesor
            reemplazo = nodo_actual.encontrarSucesor()

            reemplazo.empalmar()  # desconecta el nodo reemplazo de su lugar original
            nodo_actual.clave = reemplazo.clave
            nodo_actual.cargaUtil = reemplazo.cargaUtil

        # Nodo con un solo hijo
        else:
            hijo = nodo_actual.hijoIzquierdo if nodo_actual.tieneHijoIzquierdo() else nodo_actual.hijoDerecho
            
            if nodo_actual.esHijoIzquierdo():
                hijo.padre = nodo_actual.padre
                nodo_actual.padre.hijoIzquierdo = hijo
            elif nodo_actual.esHijoDerecho():
                hijo.padre = nodo_actual.padre
                nodo_actual.padre.hijoDerecho = hijo
            else:
                # nodo_actual es la raíz
                nodo_actual.reemplazarDatoDeNodo(
                    hijo.clave,
                    hijo.cargaUtil,
                    hijo.hijoIzquierdo,
                    hijo.hijoDerecho
                )

        
#Agrego para ver si esta balanceado.
    def esta_balanceado(self, nodo=None):
        """Devuelve True si todos los factores de equilibrio están entre -1 y 1"""
        if nodo is None:
            nodo = self.raiz #si no hay nodo uso raiz
            if nodo is None:  # Árbol vacío sin raiz ya esta balanceado
                return True

        #  si no hay nodo, ya está balanceado, hijo vacio
        if nodo is None:
            return True

        # usa feq p verificar desbalance 
        if nodo.factorEquilibrio < -1 or nodo.factorEquilibrio > 1:
            return False
        #en otro caso devuelve true
        # Llamadas recursivas a los hijos
        izq = self.esta_balanceado(nodo.hijoIzquierdo) if nodo.hijoIzquierdo else True
        der = self.esta_balanceado(nodo.hijoDerecho) if nodo.hijoDerecho else True
        #si no hay hijos --> true, xq nada va a estar desbalanceando
        return izq and der


# para probar rápido el arbol
if __name__ == "__main__":
    miArbol = ArbolAVL()

    #prueba de agregar
    miArbol.agregar(3, "tres") #clave y valor de cada nodo
    miArbol.agregar(4, "cuatro")
    miArbol.agregar(6, "seis")
    miArbol.agregar(2, "holaqtal")
    miArbol.agregar(8, ":)")
    miArbol.agregar(7, "buenas")
    miArbol.agregar(5, "soyfive")

    print(miArbol.raiz.clave) 
    print("\n¿Está balanceado?:", miArbol.esta_balanceado()) #VERIFICA BALANCE :)
    print("busco 6:", miArbol.obtener(6)) #se q existe, verifico que agrego bien #obtener devuelve valor cuando llamo clave
    print("Búsqueda de 100:", miArbol.obtener(100))  # para q devuelva None

    #prueba de "eliminar"
    miArbol.eliminar(8) #saco uno
    print("¿Está balanceado después de eliminar?:", miArbol.esta_balanceado())
    print("Buscar 8:", miArbol.obtener(8)) #verifico que elimine bien
    print(miArbol.raiz.clave) 
    #prueba empalmar: saca nodo con 2 hijos, izq y derecho
    miArbol.eliminar(3) #elijo un nodo con 2 hijos p sacar
    print("¿Está balanceado después del empalme?:", miArbol.esta_balanceado())
    print("Buscar 3:", miArbol.obtener(3)) #debe decir q no
    print("Buscar 7 :", miArbol.obtener(7)) #se q sigue estando
 #-------------------------------------------------
 #prueba accesoria para chequear balance: 
    # print(miArbol.raiz.clave) 
    # miArbol.agregar(1,1)
    # miArbol.agregar(2,2)
    # miArbol.agregar(3,3)
    # miArbol.agregar(4,4)
    # miArbol.agregar(5,5)
    # miArbol.agregar(6,6)
    # miArbol.agregar(7,7)
    # miArbol.agregar(8,8)
    # miArbol.agregar(9,9)
    # predecesor=True
    # miArbol.eliminar(6) 

    # print(miArbol.raiz.clave)
    # print(miArbol.raiz.hijoIzquierdo.clave)
    # print(miArbol.raiz.hijoDerecho.clave)

