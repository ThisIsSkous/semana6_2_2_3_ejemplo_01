"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Base de datos bddDAlencastro y coleccion pais

db = client.sk
coleccion = db.pais

# proceso que agrega una lista de documentos
listado = [
{"nombre": "Bolivia", "continente" : "latinomerica", "poblacion":"12079472"},
{"nombre": "Mexico", "continente" : "latinomerica", "poblacion":"126014024"},
{"nombre": "Argentina", "continente" : "latinomerica", "poblacion":"45808747"}
]

coleccion.insert_many(listado)
