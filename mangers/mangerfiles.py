from algorithms.normalize import normalize

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

def readAllFiles():
    """R. lee todos los archivos en un carpeta"""
    pass

def updateAFiles():
    """U. Actualizar los nombres de los archivos"""
    pass

def deleteAFiles():
    """D. Borra archivos"""
    pass

def deleteAllFiles():
    pass


