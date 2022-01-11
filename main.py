from managers.managerdir import createDir, readpathDir
from managers.mangerfiles import createFiles
from algorithms.normalizetext import cleanContent

print("UI: Iniciando programa de creación automatica, automatizada de archivos '.md' , para escribir tus notas de algun tema")

file = 'input\\texto.txt' # eN PRINCIPIO NO LE VEO INCOVENIENTO A ESTO POR AHORA
dirpath = readpathDir()
print(dirpath)
# folder = createDir('output') # y TAMPOCO LE VEO CONVENIETE A ESTE FOLDER POR AHORA
# content = cleanContent(readContent(dirpath, file))
# files = readFiles(dirpath)
# createFiles(content, folder, dirpath, 'md')
