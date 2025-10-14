class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0 #agregado !!

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self


class ArbolAVL: #maneja nodos, inserciones y rotaciones, cada nodo guarda fecha y T

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self,clave,valor): #esta queda no? creo que si 
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

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


#el agregar es igual que el ABB, se incluye "actualizar equilibrio"
    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                    self.actualizarEquilibrio(nodoActual.hijoDerecho)

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

#ROTACIONES: agregado 

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

#rotar derecha--> simetrica a rotar izq: 
    def rotarDerecha(self, rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho != None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else:
                rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz

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

    def eliminar(self,clave):
      if self.tamano > 1:
         nodoAEliminar = self._obtener(clave,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la clave no está en el árbol')
      elif self.tamano == 1 and self.raiz.clave == clave:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
       self.eliminar(clave)

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

    def remover(self,nodoActual):
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.cargaUtil = suc.cargaUtil

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)




"""miArbol = ArbolBinarioBusqueda()
miArbol[3]="rojo"
miArbol[4]="azul"
miArbol[6]="amarillo"
miArbol[2]="en"

print(miArbol[6])
print(miArbol[2]) """

# para probar rapido el arbol
if __name__ == "__main__":
    miArbol = ArbolAVL()
    miArbol.agregar(3, "rojo")
    miArbol.agregar(4, "azul")
    miArbol.agregar(6, "amarillo")
    miArbol.agregar(2, "en")

    print(miArbol.obtener(6))
    print(miArbol.obtener(2))

