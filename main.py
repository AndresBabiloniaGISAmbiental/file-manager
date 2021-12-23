
# *TODO: Refactorizar. hacer interactivo la entrada del archivo con un input
print("Iniciando programa de creación de archivos md, para escribir tus notas de algun tema")
insert_path = input("Ingresa la ruta: ")
input_file_text = open(insert_path + '\\texto.txt', 'r')
'''Esta parte tambien puede ser interactiva, el FICHERO txt'''

content = input_file_text.readlines()
'''Aqui se lee  lo que tiene el archivo en cada linea, y se guarda en la varibale content, que se convierte En una lista o array donde cada indice tiene una linea de texto y/o un salto de linea.'''
'''Abre el block de notas y guarda el contenido en la variable content, en memoria en pocas palabras, para luego en este bucle, infinito o indeterminado, al ingresar en cada linea'''
input_file_text.close()

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
''' Borro el elemento en la posicion que me indica que esta  el caracter de salto de linea. BUsco la coincidencia el salto de linea.
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
'''Aqui se crean los archivos finalmente'''
i = 0
for line in content:
    open(insert_path + f'\{i}_'+line[:len(line)-1].replace(" ", "_") + '.md','w') #crea cada
    i +=1

