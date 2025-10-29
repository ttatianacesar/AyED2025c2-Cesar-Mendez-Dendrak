 __main.py__

 
 Archivo principal del proyecto.
Ejecuta el programa general combinando las funcionalidades de los módulos:
Lee el archivo aldeas.txt y construye el grafo.
Aplica el algoritmo de Kruskal para obtener el MST.
Orienta el árbol desde una raíz elegida (por defecto, "Peligros").
Muestra por consola la distribución de noticias entre aldeas y el costo total del recorrido.


Lista de aldeas (orden alfabético):
- Aceituna
- Buenas Noches
- Cebolla
- Consuegra
- Diosleguarde
- El Cerrillo
- Elciego
- Espera
- Hortijos
- Humilladero
- La Aparecida
- La Pera
- Lomaseca
- Los Infiernos
- Malcocinado
- Melón
- Pancrudo
- Peligros
- Pepino
- Silla
- Torralta
- Villaviciosa

Distribución de noticias:
- Aceituna: recibe de -> Malcocinado; envía a -> []
- Buenas Noches: recibe de -> La Aparecida; envía a -> ['Cebolla']
- Cebolla: recibe de -> Buenas Noches; envía a -> ['Pancrudo']
- Consuegra: recibe de -> Malcocinado; envía a -> []
- Diosleguarde: recibe de -> Malcocinado; envía a -> ['Elciego']
- El Cerrillo: recibe de -> Los Infiernos; envía a -> ['Malcocinado']
- Elciego: recibe de -> Diosleguarde; envía a -> ['Melón']
- Espera: recibe de -> La Pera; envía a -> []
- Hortijos: recibe de -> Humilladero; envía a -> []
- Humilladero: recibe de -> Torralta; envía a -> ['Hortijos']
- La Aparecida: recibe de -> Peligros; envía a -> ['Buenas Noches', 'Silla']
- La Pera: recibe de -> Los Infiernos; envía a -> ['Espera']
- Lomaseca: recibe de -> Peligros; envía a -> ['Los Infiernos', 'Pepino']
- Los Infiernos: recibe de -> Lomaseca; envía a -> ['La Pera', 'El Cerrillo']
- Malcocinado: recibe de -> El Cerrillo; envía a -> ['Consuegra', 'Aceituna', 'Diosleguarde']
- Melón: recibe de -> Elciego; envía a -> []
- Pancrudo: recibe de -> Cebolla; envía a -> []
- Peligros: recibe de -> (origen - Peligros); envía a -> ['La Aparecida', 'Lomaseca']
- Pepino: recibe de -> Lomaseca; envía a -> []
- Silla: recibe de -> La Aparecida; envía a -> ['Torralta']
- Torralta: recibe de -> Silla; envía a -> ['Villaviciosa', 'Humilladero']
- Villaviciosa: recibe de -> Torralta; envía a -> []

Suma total de distancias recorridas (MST): 94



