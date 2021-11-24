#formatenado textoa md, titulos de primer nivel, eliminacion de caracteres e informaicon que no necesito
import re
ruta = 'Z:\\PROGRAMACION\\python\\app_console_formating_test\\'

input_file_text = open(ruta+'formateando_texto.txt', 'r')
content = input_file_text.readlines()
input_file_text.close()

# Expresion regular
patron = re.compile('^([01]?[0-9]|2[0-3]):[0-5][0-9]$')

## * Este pedazo de codigo funciona, borra las lineas tambien
# i = 0
# while True:
#     try:
#         if content[i] != '\n':
#             i = i+1
#         else:
#             content.pop(i)
#     except:
#         break
## ojito con borrar esto de aqui.

print(content[1], type(content[1]))
# '''Aqui se termina de formatear los archivos finalmente'''
# debo insertar una expresion regular para detectar si hay numeros y poderlo borrar


#i = 0
#for line in content:
#    '# ' + line
#    i += 1
