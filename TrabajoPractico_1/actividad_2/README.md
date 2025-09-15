# "La guerra"
Objetivo
 Implementar el juego de cartas 'Guerra', reutilizando el TAD ListaDobleEnlazada desarrollado en el Problema 1 para construir la estructura de datos Mazo, que será la base del funcionamiento del juego. 

Reutilización del Problema 1
 Del ejercicio anterior se extrajo la implementación de ListaDobleEnlazada. Esta estructura fue elegida porque permite inserciones y extracciones eficientes tanto al inicio como al final (O(1)), algo indispensable para modelar un mazo de cartas. Además, posibilita recorrer la lista y copiarla sin recurrir a estructuras nativas de Python, cumpliendo con las restricciones del enunciado.

Modelado de la carta 
La clase Carta representa cada carta del mazo con sus atributos principales: valor, palo y visible. Incluye un método privado para obtener el valor numérico, lo que permite comparaciones directas, y sobrecarga de operadores para que las comparaciones sean simples. También define métodos para su representación en pantalla. 

Finalmente, para comprobar que la implementación es correcta, se llevaron a cabo los tests proporcionados:

Test de la clase Mazo: todos los casos se ejecutaron con éxito, lo que confirma que las operaciones sobre el mazo se comportan según lo esperado.

Test del juego Guerra: todos los casos se completaron satisfactoriamente, demostrando que la lógica del juego, utilizando nuestra implementación del mazo, es sólida y cumple con los requisitos establecidos.

Se concluye que, el Problema 2 muestra cómo un TAD genérico puede reutilizarse como pieza fundamental para resolver un problema más complejo. La modularidad del código permite separar responsabilidades: Carta modela un objeto individual, Mazo gestiona la colección de cartas y JuegoGuerra orquesta las reglas. De esta forma, se respeta el paradigma de abstracción de datos y se obtiene un programa robusto, reutilizable y fácil de mantener.






> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
