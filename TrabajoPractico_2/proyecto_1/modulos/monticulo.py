# armar mi propio monticulo= menor
# La propiedad de montículo requiere que la raíz del árbol sea el ítem
#  más pequeño del árbol

class Monticulo:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanio = 0

    def insertar(self, k):
        self.listaMonticulo.append(k) #agrego al final
        self.tamanio += 1 #se incrementa el tamaño= es nuevo
        self.Infiltrar_Arriba(self.tamanio)

#si el nuevo es menor al padre, lo infiltra hacia arriba
    def Infiltrar_Arriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:   #i//2 es el padre
             tmp = self.listaMonticulo[i // 2] 
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]  #se mueve el hijo al lugar del padre
             self.listaMonticulo[i] = tmp
          i = i // 2  #padre

                                   
    def Infiltrar_Abajo(self,i):
        while (i * 2) <= self.tamanio:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm 

    def hijoMin(self,i):
        if i * 2 + 1 > self.tamanio:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def eliminarMin(self):
        if self.tamanio == 0:
            return None
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanio]
        self.tamanio -=  1
        self.listaMonticulo.pop()
        self.Infiltrar_Abajo(1)
        return valorSacado
    

    def construir_monticulo(self, una_lista):
        self.listaMonticulo = [0] + una_lista[:]      
        self.tamanio = len(una_lista)
        i = len(una_lista) // 2  
        while i > 0:
            self.Infiltrar_Abajo(i)
            i -= 1    

