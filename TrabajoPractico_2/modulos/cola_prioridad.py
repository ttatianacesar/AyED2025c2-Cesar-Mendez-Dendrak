import heapq

class ColaPrioridad:
    def __init__(self):
        self._datos = []

    def insertar(self, elemento, prioridad, desempate=0):
        # prioridad más baja = más urgente (ej: 1 crítico)
        heapq.heappush(self._datos, (prioridad, desempate, elemento))

    def eliminar(self):
        if self._datos:
            return heapq.heappop(self._datos)[2]
        return None

    def esta_vacia(self):
        return len(self._datos) == 0
