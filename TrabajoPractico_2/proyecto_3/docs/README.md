*Mostrar la lista de aldeas en orden alfabético.*
*Para cada aldea, mostrar de qué vecina debería recibir la noticia.*
*Para el envío de una noticia, mostrar la suma de todas las distancias recorridas por
todas las palomas enviadas desde cada palomar.

⚠️  Línea 57 ignorada (formato inválido): 'Diosleguarde'
Aldeas (alfabético):
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

Aristas del MST (u, v, distancia):
('Consuegra', 'Malcocinado', 1)
('Buenas Noches', 'Cebolla', 2)
('Cebolla', 'Pancrudo', 2)
('Lomaseca', 'Los Infiernos', 2)
('Aceituna', 'Malcocinado', 2)
('Elciego', 'Melón', 3)
('Espera', 'La Pera', 3)
('Buenas Noches', 'La Aparecida', 3)
('La Pera', 'Los Infiernos', 3)
('Lomaseca', 'Pepino', 3)
('Silla', 'Torralta', 4)
('La Aparecida', 'Peligros', 5)
('La Aparecida', 'Silla', 5)
('El Cerrillo', 'Lomaseca', 5)
('Hortijos', 'Humilladero', 5)
('El Cerrillo', 'Malcocinado', 6)
('Diosleguarde', 'Elciego', 7)
('Lomaseca', 'Peligros', 7)
('Torralta', 'Villaviciosa', 8)
('Humilladero', 'Torralta', 9)
('Diosleguarde', 'Malcocinado', 9)
Peso total del MST (suma de distancias): 94

Envíos por aldea (padre -> hijos) y sumas enviadas desde cada palomar:
Aldea: Aceituna
  recibe de: Malcocinado
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Buenas Noches
  recibe de: La Aparecida
  envía a: ['Cebolla']
  distancia total enviada desde su palomar: 2

Aldea: Cebolla
  recibe de: Buenas Noches
  envía a: ['Pancrudo']
  distancia total enviada desde su palomar: 2

Aldea: Consuegra
  recibe de: Malcocinado
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Diosleguarde
  recibe de: Malcocinado
  envía a: ['Elciego']
  distancia total enviada desde su palomar: 7

Aldea: El Cerrillo
  recibe de: Lomaseca
  envía a: ['Malcocinado']
  distancia total enviada desde su palomar: 6

Aldea: Elciego
  recibe de: Diosleguarde
  envía a: ['Melón']
  distancia total enviada desde su palomar: 3

Aldea: Espera
  recibe de: La Pera
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Hortijos
  recibe de: Humilladero
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Humilladero
  recibe de: Torralta
  envía a: ['Hortijos']
  distancia total enviada desde su palomar: 5

Aldea: La Aparecida
  recibe de: Peligros
  envía a: ['Buenas Noches', 'Silla']
  distancia total enviada desde su palomar: 8

Aldea: La Pera
  recibe de: Los Infiernos
  envía a: ['Espera']
  distancia total enviada desde su palomar: 3

Aldea: Lomaseca
  recibe de: Peligros
  envía a: ['Los Infiernos', 'Pepino', 'El Cerrillo']
  distancia total enviada desde su palomar: 10

Aldea: Los Infiernos
  recibe de: Lomaseca
  envía a: ['La Pera']
  distancia total enviada desde su palomar: 3

Aldea: Malcocinado
  recibe de: El Cerrillo
  envía a: ['Consuegra', 'Aceituna', 'Diosleguarde']
  distancia total enviada desde su palomar: 12

Aldea: Melón
  recibe de: Elciego
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Pancrudo
  recibe de: Cebolla
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Peligros
  recibe de: None
  envía a: ['La Aparecida', 'Lomaseca']
  distancia total enviada desde su palomar: 12

Aldea: Pepino
  recibe de: Lomaseca
  envía a: []
  distancia total enviada desde su palomar: 0

Aldea: Silla
  recibe de: La Aparecida
  envía a: ['Torralta']
  distancia total enviada desde su palomar: 4

Aldea: Torralta
  recibe de: Silla
  envía a: ['Villaviciosa', 'Humilladero']
  distancia total enviada desde su palomar: 17

Aldea: Villaviciosa
  recibe de: Torralta
  envía a: []
  distancia total enviada desde su palomar: 0

Suma total de distancias (verificación): 94
Nota: debe coincidir con peso total del MST.
