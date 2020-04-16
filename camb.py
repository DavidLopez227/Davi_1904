#Parte 1
#Grupo 4
#creado por: 
#Luis David López Raquec


import os
from os import path
import shutil
import json

# destino donde seran extraidos los archivos(jpg)
Source_Path = '/Users/DELL LATITUDE/Desktop/EjercicioC/imagenes'
# destino donde seran inportadis los nuevos cambios de cada archivo
Destination = '/Users/DELL LATITUDE/Desktop/EjercicioC/imagenes/1'
def main():
    count = 1
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  "Ejemplo_" + str(count) + ".jpg"
        # usa un for para cambiar el nombre de cada archivo de la carpeta uno o varios
        # renombra a todos los archivos dentro de la carpeta o Destino
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination))
# codigo de de conductor Usando una la fucncion main
if __name__ == '__main__':
    main()

#with open('CambioNombre.json', 'w') as archivo:
#    json.dump(dst, archivo)
#    print('Archivo Exportado')

  
    
