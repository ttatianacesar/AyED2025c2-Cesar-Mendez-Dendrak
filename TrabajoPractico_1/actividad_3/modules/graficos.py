# -------------------------
import matplotlib.pyplot as plt
# Graficar resultados
# -------------------------
def graficar_resultados(tamaños, tiempos_burbuja, tiempos_quick, tiempos_radix, tiempos_sorted):
    plt.figure(figsize=(12,6))
    plt.plot(tamaños, tiempos_burbuja, label='Bubble Sort')
    plt.plot(tamaños, tiempos_quick, label='QuickSort')
    plt.plot(tamaños, tiempos_radix, label='Radix Sort')
    plt.plot(tamaños, tiempos_sorted, label='Python sorted')
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo (s)")
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.legend()
    plt.grid(True)
    plt.show()
