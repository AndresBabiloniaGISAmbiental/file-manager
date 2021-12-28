from managerdir import createDir, readDir
from mangerfiles import createFiles


# TODO: Me gustaria implementar una funcion que tenga un temporizador si llega a cero entonces crea una carpeta por defecto
print("UI: Iniciando programa de creación automatica, automatizada de archivos '.md' , para escribir tus notas de algun tema")

# *TODO Esta parte tambien puede ser interactiva, el FICHERO txt
def generateContent(dirpath):
    open_file_text = open(dirpath + '\\texto.txt', 'r', encoding="utf-8")
    content = open_file_text.readlines()
    print(content)
    open_file_text.close()
    '''Aqui se lee  lo que tiene el archivo en cada linea, y se guarda en la varibale content, que se convierte En una lista o array donde cada indice tiene una linea de texto y/o un salto de linea.'''
    '''Abre el block de notas y guarda el contenido en la variable content, en memoria en pocas palabras, para luego en este bucle, infinito o indeterminado, al ingresar en cada linea'''
    """ Delete line with cero or  empyty, empity whatever"""
    # open(path+"\\texto2.txt", 'w')
    i = len(content)-1
    '''Establezco el contado, no se porque le quito 1, creo que es por ensayo y error..empiezo por la ultima linea'''
    while  True:
        try:
            if content[i] != '\n' and i <= len(content):
                i = i-1
            else:
                content.pop(i)
        except:
            break
    ''' Borro el elemento en la posicion que me indica que esta  el caracter de salto de linea. Busco la coincidencia el salto de linea.
    limpieza del archivo de saltos de lineas, para dejar solo el texto util.'''
    #TODO Refactorizar el while por un for si se quiere.
    return content


dirpath = readDir()
folder = createDir()
content = generateContent(dirpath)
createFiles(content, folder, dirpath)
