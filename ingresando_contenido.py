import os
import pathlib
#formatenado textoa md, titulos de primer nivel, eliminacion de caracteres e informaicon que no necesito
import re
ruta = pathlib.Path(__file__).parent.absolute()
# input_file_text = open(str(ruta)+'\\formateando_texto.txt', 'r')
# content = input_file_text.readlines()
# input_file_text.close()

# Expresion regular
patron = re.compile('^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
print(patron)
# debo insertar una expresion regular para detectar si hay numeros y poderlo borrar

# Ahora necesito leer la carpeta y los archivos para elejir a cual archivo le voy a meter los datos que tengo
# en el otro archivo de texto

#i = 0
#for line in content:
#    '# ' + line
#    i += 1

# Seleccione un archivo
content_of_dir = os.scandir(ruta)

folder_of_dir = []
files_markdown = []
for item in content_of_dir:
    if os.path.isdir(os.path.join(ruta, item)):
        folder_of_dir.append(item)
    else:
        if os.path.isfile(os.path.join(ruta, item)) and item.endswith('.md'):
            files_markdown.append(item)
        pass

print(folder_of_dir)
print(files_markdown)
"Listo esta funcion funciona, seleccion los archivos markdown"

