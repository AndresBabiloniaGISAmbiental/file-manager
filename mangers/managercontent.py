import os
import pathlib
#formatenado textoa md, titulos de primer nivel, eliminacion de caracteres e informaicon que no necesito
import re

from managerdir import readpathDir

def readContent(dirpath, file):
    input_file_text = open(f'{dirpath}\{file}', 'r', encoding="utf-8")
    content = input_file_text.readlines()
    input_file_text.close()
    return content

def readFolderAndFiles(dirpath):
    "R. Folder and files in a specific path"
    dir_readed = os.listdir(dirpath)
    folder_of_dir = []
    files_markdown = []
    for item in dir_readed:
        if os.path.isdir(os.path.join(dirpath, item)):
            folder_of_dir.append(item)
        else:
            if os.path.isfile(os.path.join(dirpath, item)) and item.endswith('.md'):
                files_markdown.append(item)
    return folder_of_dir, files_markdown




# Expresion regular
patron = re.compile('^([01]?[0-9]|2[0-3]):[0-5][0-9]$')
# debo insertar una expresion regular para detectar si hay numeros y poderlo borrar
