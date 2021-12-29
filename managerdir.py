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
    """R. Read de curretn dir of this script"""
    dirpath = str(pathlib.Path(__file__).parent.absolute())
    return dirpath


def updateDir(namedir):
    """U. Rename a Dir"""
    (namedir)
    pass

def deleteDir(namedir):
    """D. Borra todo un directorio con el contenido incluido"""
    try:
        shutil.rmtree(namedir)
    except OSError as e:
        print(f"Error:{ e.strerror}, otergue permisos necesarios o el directorio no")

