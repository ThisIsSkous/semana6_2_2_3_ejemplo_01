"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.sk
coleccion = db.ciudad

print("Borrar registros de Bolivia")
coleccion.delete_many({'paisPertenencia':'Bolivia'})

print("Indicar informacion")
datos = coleccion.find()
for registro in datos:
    print(registro)
