class Paciente:
    contador = 0  # sirve para diferenciar orden de llegada

    def __init__(self, nombre, riesgo):
        self.nombre = nombre
        self.riesgo = riesgo  # 1 crítico, 2 moderado, 3 bajo
        self.llegada = Paciente.contador
        Paciente.contador += 1

    def __repr__(self):
        return f"Paciente({self.nombre}, riesgo={self.riesgo}, llegada={self.llegada})"

