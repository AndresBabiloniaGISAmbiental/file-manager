import shutil
import pathlib
import os

def createDir():
    '''C. Se Crea el directorio donde se van a guardar los archivos .md'''
    try:
        name_of_folder = input(
            "Ingrese el nombre de la carpeta que desea crear: ")
        os.mkdir(f'{name_of_folder}')
    except FileExistsError:
        print("Carpeta ya existe, no se creo")
    return name_of_folder

def readpathDir():
    """R. """
    dirpath = str(pathlib.Path(__file__).parent.absolute())
    return dirpath


def updateDir():
    """U. Rename a Dir"""
    pass

def deleteDir(dir):
    """D. """
    dirPath = dir
    try:
        shutil.rmtree(dirPath)
    except OSError as e:
        print(f"Error:{ e.strerror}")


deleteDir('aa')
deleteDir('bb')
deleteDir('cc')
deleteDir('dd')
deleteDir('ff')
