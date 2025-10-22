

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    if n == 0:
        return
    output = [0] * n
    count = [0] * 10  # dígitos 0-9

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Validaciones y casos triviales
    if not isinstance(arr, list):
        raise TypeError("radix_sort espera una lista de enteros no negativos.")
    if len(arr) == 0: #chqueo p que no este vacio
        return arr  # evita ValueError en max()
    # comprobar si hay negativos 
    for x in arr:
        if x < 0:
            raise ValueError("radix_sort (implementación actual) no soporta números negativos.")

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr


# -------------------------
# PRUEBAS UNITARIAS
# -------------------------
if __name__ == "__main__":
    import random

    print("\n=== PRUEBAS: RADIX SORT ===")

    pruebas = [
        [],                         # vacía
        [42],                       # 1 elemento
        [1, 2, 3, 4, 5],            # ya ordenada
        [5, 4, 3, 2, 1],            # reversa
        [3, 1, 2, 3, 1],            # repetidos
        random.sample(range(1, 100), 10),             # aleatoria pequeña
        [random.randint(10000, 99999) for _ in range(500)]  # 500 números de 5 dígitos
    ]

    for i, lista in enumerate(pruebas, 1):
        # hacemos copia porque la función ordena in-place
        copia = lista.copy()
        try:
            resultado = radix_sort(copia)
            ok = resultado == sorted(lista)
        except Exception as e:
            ok = False
            print(f"Prueba {i}: EXCEPCIÓN -> {e}")
            continue
        print(f"Prueba {i}: {'OK' if ok else 'FALLO'}")

