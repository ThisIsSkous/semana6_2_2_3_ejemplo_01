"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Base de datos bddDAlencastro y coleccion ciudad

db = client.sk
coleccion = db.ciudad

# proceso que agrega una lista de documentos
listado = [
{"nombre": "El Alto", "paisPertenencia" : "Bolivia", "Poblacion":"1089100"},
{"nombre": "Tijuana", "paisPertenencia" : "Mexico", "Poblacion":"1810645"},
{"nombre": "Córdoba", "paisPertenencia" : "Argentina", "Poblacion":"1317298"},
]

coleccion.insert_many(listado)
