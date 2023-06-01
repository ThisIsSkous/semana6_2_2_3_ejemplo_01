"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección pais de bddDAlencastro

db = client.sk
coleccion = db.ciudad

print("Datos de ciudad")
datos = coleccion.find()
for registro in datos:
    print(registro)
