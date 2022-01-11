import shutil
import pathlib
import os

def createDir(namedir):
    '''C. Se Crea el directorio donde se van a guardar los archivos .md'''
    try:
        os.mkdir(f'{namedir}')
    except FileExistsError:
        print("Carpeta con ese nombre ya existe, no se creo, intente con otro nombre")
    return namedir

def readpathDir():
    # ! Error de logica porque lee el directorio actual, pero no sirve asi
    # * La idea es que lea el directorio de forma dinamica
    """R. Read the current dir where is this script that where"""
    dirpath = str(pathlib.Path(__file__).parent.absolute())
    # dirpath = ""
    return dirpath

def readDir():
    " Lee el directorio sin contar la carpeta en la que se ejecuta este script"
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return current_dir

def readFolders(dirpath):
    "R. Folders in a specific path"
    dir_readed = os.listdir(dirpath)
    folder_of_dir = []
    for item in dir_readed:
        if os.path.isdir(os.path.join(dirpath, item)):
            folder_of_dir.append(item)
    return folder_of_dir

def readCurrentDir():
    a = readpathDir()
    current_dir = a[len(readDir()):]
    print(current_dir)
    return current_dir

# TODO: Finishi this functions
def updateDir(namedir):
    """U. Rename a Dir"""
    (namedir)
    pass

def deleteDir(namedir):
    """D. Borra todo un directorio con el contenido incluido"""
    try:
        shutil.rmtree(namedir)
    except OSError as e:
        print(f"Error:{ e.strerror}, otergue permisos necesarios o el directorio no existe")

# TODO: Finishi this functions
def searchAllDir():
    pass

# TODO: Finishi this functions
def searchSingleDir():
    pass


a = readCurrentDir()
