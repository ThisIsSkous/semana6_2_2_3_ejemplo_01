"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.sk
coleccion = db.pais

print("Borrar registros de latinomerica")
coleccion.delete_many({'continente':'latinomerica'})

print("Indicar informacion")
datos = coleccion.find()
for registro in datos:
    print(registro)
