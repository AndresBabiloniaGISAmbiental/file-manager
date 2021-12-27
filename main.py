import pathlib
import os

# ? Debo meter todas estaos pasos logicos en funciones?
print("UI: Iniciando programa de creación de archivos md, para escribir tus notas de algun tema")
a = pathlib.Path(__file__).parent.absolute()
path = str(a)
try:
    name_of_folder = input("Ingrese el nombre de la carpeta que desea crear: ")
    os.mkdir(f'{name_of_folder}')
except FileExistsError:
    print("Carpeta ya existe, no se creo")
'''Se Crea el directorio donde se van a guardar los archivos .md, de manera dinamica e interactiva, por linea de comando por CLI'''
# TODO: Me gustaria implementar una funcion que tenga un temporizador si llega a cero entonces crea una carpeta por defecto

# *TODO Esta parte tambien puede ser interactiva, el FICHERO txt
open_file_text = open(path + '\\texto.txt', 'r')
content = open_file_text.readlines()
open_file_text.close()
'''Aqui se lee  lo que tiene el archivo en cada linea, y se guarda en la varibale content, que se convierte En una lista o array donde cada indice tiene una linea de texto y/o un salto de linea.'''
'''Abre el block de notas y guarda el contenido en la variable content, en memoria en pocas palabras, para luego en este bucle, infinito o indeterminado, al ingresar en cada linea'''

i = len(content)-1
'''Establezco el contado, no se porque le quito 1, creo que es por ensayo y error..empiezo por la ultima linea'''
while  True:
    try:
        if content[i] != '\n' and i <= len(content):
            i = i-1
        else:
            content.pop(i)
    except:
        break
''' Borro el elemento en la posicion que me indica que esta  el caracter de salto de linea. Busco la coincidencia el salto de linea.
limpieza del archivo de saltos de lineas, para dejar solo el texto util.'''
#TODO Refactorizar el while por un for si se quiere.

# j = 0
# lon_conten = (len(content))
# for line in content:
#     # BUsco la coincidencia el salto de linea.
#     if line == '\n' and j <= lon_conten:
#         content.pop(j)
#         j += 1
#         print(len(content))

i = 0
for line in content:
    try:
        name_file = str(line[:len(line)-1].replace(" ", "_"))
        open(path+ f'\{name_of_folder}' + f'\{i}_'+ name_file + '.md','w')
        i +=1
    except:
        print("Se produjo un error")
'''Aqui se crean los archivos finalmente, enumerados desde el 0'''

