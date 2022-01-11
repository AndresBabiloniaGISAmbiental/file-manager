
#formatenado textoa md, titulos de primer nivel, eliminacion de caracteres e informaicon que no necesito
import re

from managers.managerdir import readpathDir

def readContent(dirpath, file):
    input_file_text = open(f'{dirpath}{file}', 'r', encoding="utf-8")
    content = input_file_text.readlines()
    input_file_text.close()
    return content


# Expresion regular
patron = re.compile('^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
# debo insertar una expresion regular para detectar si hay numeros y poderlo borrar
