from normalize import normalize

def createFiles(content, folder, dirpath):
    '''creacion de archivos .md'''
    i = 1
    for line in content:
        try:
            s = line[:len(line)-1]
            name_file = normalize(s)
            print(name_file)
            open(dirpath + f'\{folder}' + f'\{i}_' + name_file + '.md', 'w')
            i += 1
        except OSError as err:
            print("Se produjo un error:", err)
