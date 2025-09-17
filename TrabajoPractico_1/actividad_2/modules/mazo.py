from modules.ListaDobleEnlazada import ListaDobleEnlazada  

class DequeEmptyError(Exception):
    """Error lanzado al intentar sacar una carta de un mazo vacío."""
    pass


class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()

    def __len__(self):
        return len(self._cartas)

    def esta_vacio(self):
        return len(self._cartas) == 0

    def poner_carta_arriba(self, carta):
        """Inserta una carta en la parte superior (al inicio)."""
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Coloca una carta en la parte inferior (al final)."""
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Saca y devuelve la carta superior (cabeza).
        Si mostrar=True, marca la carta como visible.
        """
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        carta = self._cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __str__(self):
        """Representación del mazo (cubre caso vacío)."""
        if self.esta_vacio():
            return "[mazo vacío]"
        return " ".join(str(carta) for carta in self._cartas)


if __name__=="__main__":
    m=Mazo()