import json
base_de_datos = []

def precio():
    motocicleta = 15
    return(motocicleta)
def precio():
    automovil = 30
    return(automovil)
def precio():
    camioneta = 50
    return(camioneta)   
def descuento():
    if cliente == 'miembro':
        descu = (precio() * 0.10)
    return(miembro)
def descuento():
    if comparacion == 'si':
        descu = (precio() * 0.10)
    return(descuento)
def total():
    descuento = (precio() * 0.10)
    tot = (precio() - descuento)
    return(total)

veces = int(input("Ingres la cantidad de Ventas: "))
for i in range(veces):
    ventas = {}

    vehiculo = input('Ingrese el tipo de vehiculo: ')
    cliente = input('Ingrese el tipo de cliente: ')
    comparacion = input('Fin de Semana? Si o No: ')

    ventas['Vehiculo'] = vehiculo
    ventas['Precio'] = precio()
    ventas['Cliente'] = cliente
    ventas['Fin de Semana'] = comparacion

    base_de_datos.append(ventas)

print(base_de_datos)

with open('car_wash.json', 'w') as archivo:
    json.dump(base_de_datos, archivo)
    print('Archivo Exportado')
