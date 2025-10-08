import time
import datetime
import modulos.paciente as pac
import modulos.cola_prioridad as cp
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = cp.ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Crear paciente
    paciente = pac.Paciente()

    # Insertar en la cola de prioridad (riesgo es la prioridad)
    cola_de_espera.insertar(paciente, paciente.riesgo, paciente.tiempo_llegada)

    # 50% de probabilidad de atender a alguien
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        paciente_atendido = cola_de_espera.eliminar()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)

    print()
    print('Pacientes que faltan atenderse:', len(cola_de_espera.datos))
    for prioridad, desempate, paciente in cola_de_espera.datos:
        print('\t', paciente)

    print()
    print('-*-' * 15)
    time.sleep(1)
