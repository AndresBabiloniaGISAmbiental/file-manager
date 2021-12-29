def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("\\",""),
        ("?", ""),
        ("¿", ""),
        ("/",""),
        (":",""),
        ("*",""),
        ('"',""),
        ("<",""),
        (">",""),
        ("|",""),
        (" ", "_")
        )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def cleanContent(content):
    '''Establezco el contado, no se porque le quito 1, creo que es por ensayo y error..empiezo por la ultima linea'''
    i = len(content)-1
    while True:
        try:
            if content[i] != '\n' and i <= len(content):
                i = i-1
            else:
                content.pop(i)
        except:
            break
    ''' Borro el elemento en la posicion que me indica que esta  el caracter de salto de linea. Busco la coincidencia el salto de linea.
    limpieza del archivo de saltos de lineas, para dejar solo el texto util.'''
    return content
