
from modulos.monticulo import Monticulo


class ColaPrioridad:
    def __init__(self):
        self.monticulo = Monticulo()

    def encolar(self, item):
        self.monticulo.insertar(item)

    def desencolar(self):
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        return self.monticulo.tamanio==0

    def __len__(self):
        return self.monticulo.tamanio
    
    def __iter__(self):
        for item in self.monticulo.listaMonticulo[1:]:
            yield item
