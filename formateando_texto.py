import pathlib
#formatenado textoa md, titulos de primer nivel, eliminacion de caracteres e informaicon que no necesito
import re
ruta = pathlib.Path(__file__).parent.absolute()
input_file_text = open(str(ruta)+'\\formateando_texto.txt', 'r')
content = input_file_text.readlines()
input_file_text.close()

# Expresion regular
patron = re.compile('^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
# debo insertar una expresion regular para detectar si hay numeros y poderlo borrar

# Ahora necesito leer la carpeta y los archivos para elejir a cual archivo le voy a meter los datos que tengo
# en el otro archivo de texto

#i = 0
#for line in content:
#    '# ' + line
#    i += 1
