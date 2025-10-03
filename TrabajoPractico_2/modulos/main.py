from paciente import Paciente
from cola_prioridad import ColaPrioridad

def main():
    cola = ColaPrioridad()

    # Simulación: llegan pacientes
    p1 = Paciente("Juan", 2)
    p2 = Paciente("Ana", 1)
    p3 = Paciente("Pedro", 3)
    p4 = Paciente("Lucía", 1)

    # Insertamos en la cola con riesgo como prioridad y llegada como desempate
    cola.insertar(p1, p1.riesgo, p1.llegada)
    cola.insertar(p2, p2.riesgo, p2.llegada)
    cola.insertar(p3, p3.riesgo, p3.llegada)
    cola.insertar(p4, p4.riesgo, p4.llegada)

    print("Atendiendo pacientes en orden de prioridad:")
    while not cola.esta_vacia():
        paciente = cola.eliminar()
        print(f"Atendido: {paciente}")

if __name__ == "__main__":
    main()
