from managercontent import readContent
from managerdir import createDir, readpathDir
from mangerfiles import createFiles
from normalize import cleanContent


print("UI: Iniciando programa de creación automatica, automatizada de archivos '.md' , para escribir tus notas de algun tema")


file = 'texto.txt'
dirpath = readpathDir()
folder = createDir('aa')
content = cleanContent(readContent(dirpath, file))

createFiles(content, folder, dirpath, 'md')
