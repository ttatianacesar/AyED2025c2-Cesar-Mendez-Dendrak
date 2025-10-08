import heapq

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def insertar(self, item):
        heapq.heappush(self.elementos, item)

    def eliminar(self):
        if len(self.elementos) > 0:
            return heapq.heappop(self.elementos)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        return iter(sorted(self.elementos))
