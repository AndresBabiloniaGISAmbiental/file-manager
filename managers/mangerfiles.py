from algorithms.normalizetext import normalize
import os
import pathlib

def createFiles(content, folderCustom, dirpath, ext):
    '''C. creacion de archivos de cualquier formato'''
    i = 1
    for line in content:
        try:
            s = line[:len(line)-1]
            name_file = normalize(s)
            open(f'{dirpath}\{folderCustom}\{i}_{name_file}.{ext}', 'w')
            i += 1
        except OSError as err:
            print("Se produjo un error:", err)

def readFiles1ext(dirpath, ext):
    "R. names of files in a specific path with especific extension"
    dir_readed = os.listdir(dirpath)
    files_ext = []
    for item in dir_readed:
        if os.path.isfile(os.path.join(dirpath, item)) and item.endswith(ext):
            files_ext.append(item)
        return files_ext

def readFilesAllext(dirpath):
    """R. lee todos los archivos en un carpeta"""
    dir_readed = os.listdir(dirpath)
    files_all_ext = []
    for item in dir_readed:
        if os.path.isfile(os.path.join(dirpath, item)):
            files_all_ext.append(item)
        return files_all_ext

def updateAFiles():
    """U. Actualizar los nombres de los archivos"""
    pass

def deleteAFiles():
    """D. Borra archivos"""
    pass

def deleteAllFiles():
    pass


