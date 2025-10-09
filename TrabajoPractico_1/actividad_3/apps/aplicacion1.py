# Aplicación secundaria

# -------------------------
# Ejecutar pruebas
# -------------------------
from modules.ordenamiento import bubble_sort, quicksort, radix_sort
from modules.utilidades import generar_lista, medir_tiempo
from modules.graficos import graficar_resultados 

# Pruebas básicas de funcionamiento
def probar_algoritmos():
    # --- Prueba básica con lista corta ---
    prueba = [5, 3, 8, 1, 2]
    print("Lista original:", prueba)
    print("Bubble Sort:", bubble_sort(prueba.copy()))
    print("QuickSort:", quicksort(prueba.copy()))
    print("Radix Sort:", radix_sort(prueba.copy()))

    # --- Prueba con lista grande de 500 números aleatorios ---
    print("\nVerificando funcionamiento con 500 números aleatorios...")
    lista_prueba = generar_lista(500)
    print("Lista original (primeros 10):", lista_prueba[:10])

    ordenada_bubble = bubble_sort(lista_prueba.copy())
    ordenada_quick = quicksort(lista_prueba.copy())
    ordenada_radix = radix_sort(lista_prueba.copy())

    print("Bubble Sort OK:", ordenada_bubble == sorted(lista_prueba))
    print("QuickSort OK:", ordenada_quick == sorted(lista_prueba))
    print("Radix Sort OK:", ordenada_radix == sorted(lista_prueba))


# Medición de tiempos
def medir_y_graficar():
    tamaños = list(range(1, 1001))
    tiempos_burbuja = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = []


    print("Midiendo tiempos, esto puede tardar un poco...")

    for n in tamaños:
        lst = generar_lista(n)
        tiempos_burbuja.append(medir_tiempo(bubble_sort, lst))
        tiempos_quick.append(medir_tiempo(quicksort, lst))
        tiempos_radix.append(medir_tiempo(radix_sort, lst))
        tiempos_sorted.append(medir_tiempo(sorted, lst))

    graficar_resultados(tamaños, tiempos_burbuja, tiempos_quick, tiempos_radix, tiempos_sorted)
# -------------------------
# Complejidad a priori
# -------------------------
print("\nComplejidades teóricas:")
print("Bubble Sort: O(n^2)")
print("QuickSort: O(n log n) promedio, O(n^2) peor caso")
print("Radix Sort: O(d·n), d = número de dígitos")
print("Python sorted (Timsort): O(n log n) en el peor caso")

if __name__ == "__main__":
    probar_algoritmos()
    medir_y_graficar()