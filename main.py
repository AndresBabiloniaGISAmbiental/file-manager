from managercontent import readContent, readFolderAndFiles
from managerdir import createDir, readpathDir
from mangerfiles import createFiles
from algorithms.normalize import cleanContent

print("UI: Iniciando programa de creación automatica, automatizada de archivos '.md' , para escribir tus notas de algun tema")

file = 'texto.txt'
dirpath = readpathDir()
folder = createDir('aa')
content = cleanContent(readContent(dirpath, file))
folders, files = readFolderAndFiles(dirpath)
createFiles(content, folder, dirpath, 'md')
