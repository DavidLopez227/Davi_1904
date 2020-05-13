from collections import deque
import json

# definir la cola

cola = deque()
print('Ingrese el número de archivo que desea agregar a la cola: ')
print('')
print('[1] Archivo1.txt')
print('[2] Archivo2.txt')
print('[0] Cancelar')
print('')

opcion = int(input("> "))
if opcion == 1:
        elige = "Archivo1.txt"
elif opcion == 2:
        elijeUsuario = "Archivo2.txt"
elif opcion == 0:
        elijeUsuario = "Cancelar"
# agregar elementos
print("La cola de impresión es: ")
print(elijeUsuario)

print('')
print('Desea? ')
print('')
print('1) Agregar un elemento a la cola de impresion')
print('2) Imprimir')
print('3) Salir')
print('')
opcion = int(input("> "))
if opcion == 1:
        elige = "Agregar"
elif opcion == 2:
        elijeUsuario = "Imprimir"
elif opcion == 0:
        elijeUsuario = "Salir"
print('Se encontraron los siguentes archivos en la carpeta actual')
print('Ingrese el número de archivo que desea agregar a la cola: ')
print('')
print('[1] Archivo1.txt')
print('[2] Archivo2.txt')
print('[0] Cancelar')
print('')
opcion = int(input("> "))
if opcion == 1:
        elige = "Archivo1.txt"
elif opcion == 2:
        elijeUsuario = "Archivo2.txt"
elif opcion == 0:
        elijeUsuario = "Cancelar"

cola.append(elige, opcion)
cola.append(elige, opcion)

print(f'Cola de impresión: {cola}')
print("#########")


while len(cola) > 0:
    # extraer el primer elemento en la cola
    siguiente_elemento = cola.popleft()


    print(f'Siguiente elemento: {siguiente_elemento}')
    print(f'Cola de impresión: {cola}')
    print("#########")
