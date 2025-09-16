El objetivo principal es implementar la clase Mazo utilizando la estructura ListaDobleEnlazada previamente desarrollada, y verificar su funcionamiento dentro de la simulación del juego Guerra.
-Estructura del programa-
Carta (carta.py): representa cada carta con atributos valor, palo y visible.
  Incluye método privado _valor_numerico() para comparaciones (2–10, J=11, Q=12, K=13, A=14).
  Sobrecarga de operadores para simplificar comparaciones.
  Representación en pantalla: -X si está oculta, o valor+palo si es visible.
ListaDobleEnlazada (ListaDobleEnlazada.py): estructura base del mazo.
  Operaciones principales: inserción/extracción al inicio o final en O(1); inserción/extracción      intermedia en O(n).
  Métodos: esta_vacia(), agregar_al_inicio(), agregar_al_final(), extraer(), copiar(), invertir(),   concatenar().
  Atributos: cabeza, cola, tamanio.
Mazo (mazo.py): encapsula una ListaDobleEnlazada en _cartas.
  poner_carta_arriba(carta) — O(1).
  poner_carta_abajo(carta) — O(1).
  sacar_carta_arriba(mostrar=False) — O(1); lanza DequeEmptyError si está vacío.
  esta_vacio(), __len__(), __str__().
  Excepción DequeEmptyError definida según la consigna.
JuegoGuerra (juegoguerra.py): coordina la lógica del juego.
  Arma el mazo inicial (52 cartas barajadas con seed).
  Reparte cartas equitativamente entre dos jugadores.
  Ejecuta turnos: cada jugador saca la carta superior, se comparan y el ganador acumula las  cartas.
  En caso de empate: cada jugador coloca 3 cartas boca abajo y otra visible para desempatar.
  Si un jugador se queda sin cartas durante la guerra, se lanza DequeEmptyError y gana el otro.
  Límite de turnos: N_TURNOS = 10000 para evitar bucles infinitos.
  Aspectos destacados
  La lista doblemente enlazada fue elegida porque permite operaciones rápidas en ambos extremos,   fundamentales para el manejo del mazo.
  La clase carta implementa sobrecarga de operadores para simplificar comparaciones.
  El juego finaliza cuando un jugador obtiene todas las cartas o se llega al límite de turnos.
  El diseño modular separa responsabilidades:
  Carta modela un objeto individual.
  Mazo gestiona la colección de cartas.
  JuegoGuerra orquesta las reglas.
Esto demuestra cómo un TAD genérico puede reutilizarse para resolver problemas más complejos, asegurando un código robusto, reutilizable y mantenible.

El pseudocodigo es el siguiente:
INICIO
Crear mazo con 52 cartas (valores 2–A y 4 palos)
Mezclar el mazo
Repartir 26 cartas a cada jugador
MIENTRAS ambos jugadores tengan cartas Y no se supere el límite de turnos:
    Jugador 1 saca carta superior
    Jugador 2 saca carta superior
    SI carta1 > carta2:
        Jugador 1 coloca ambas cartas al final de su mazo
    SINO SI carta2 > carta1:
        Jugador 2 coloca ambas cartas al final de su mazo
    SINO:
        DECLARAR "GUERRA"
        Cada jugador coloca 3 cartas boca abajo (si las tiene)
        Cada jugador coloca 1 carta visible
        Comparar nuevamente (el ganador se lleva todas las cartas en juego)
FIN MIENTRAS
SI un jugador quedó sin cartas:
    Declarar ganador al otro jugador
SINO SI se llegó al límite de turnos:
    Declarar empate
FIN






