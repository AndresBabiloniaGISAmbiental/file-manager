# DEVELOP

## DESCRIPCION DEL PROBLEMA O NECESIDAD 1

Realizar el codigo para que el programa haga lo siguiente:

Cuando tenga Tener un archivo de texto,cuyo contenido sean los titulos de Primer nivel, el programa debera tratar el texto si viene con datos o caracteres de texto extraños que no queremos que aparezca, es decir tratarlos y dejarlos limpios para luegos insertarlos en algun archivo markdown.

**Ejemplos:**

Que tenga texto de hora en el titulo como `04:20` entre otros tipo de formatos.
Cambiar los caracteres raro a tildes si es necesarios.

[ok] Crud de archivos
[ok] Crud de carpetas o foldes

## OBJETIVOS

### OBJETIVO GENERAL

Realizar un CRUDS del contenido, en el archivo markdown de eleccion o preferencia.

### OBJETIVO ESPECIFICO

1. CREATE: Introduccion el contenido con formato markdown en un arhcivo markdown proveniente de un block de notas
   * 🗒️ Leer todos los archivos (`.md`) generados, anteriormente, esto los puedo y almacenarlo en el codigo en alguna variables es decir en memoria ram, o tamien puedo guardarlo en algun block de nota, o archivo serializado, o incluso en una base de datos, como SQL, ¿sera que tengo que darle un ID o un identificador, en fin despues reviso que es mejor?.
   * 👉 Elegir uno de los archivos (`.md`) a modificar, (tal vez por su ID, debo darle un ID?)
   * Leer el contenido en el archivo.
   * Eliminar el contenido no deseado, no compatible.
   * Crear Agregar o formatear el contenido compatible con markdown.
     Ejemplo: `# Introduccion`, `# Primeros pasos`
   * 📋 Insertar el contenido que quiero en el archivo.

2. 👀 READ:
   * Ver o Leer todos los archivos (`.md`) disponibles.
   * Seleccionar el archivo md de preferencia.
   * Ver el contenido que inserte.

3. UPDATE:
    * 🗒️ Ver o Leer todos los archivos (`.md`) disponibles.
    * Seleccionar el archivo md de preferencia.
    * Insertarle al informacion nueva que quiero o borrarla.

4. 🗑️ DELETE:
    * Eliminiar el contenido que inserte.
    * PASS

5. 🔎 SEARCH:
   * Buscar contenido, segun algun criterio, sera que este se asemeja al read?
   * Aqui hay verbos tambien de apoyo a estas actividades como, busqueda y ordenamiento

# COMENTARIOS DEL CODIGÓ (DESORDENADAMENTE)

Listo esta funcion funciona, LEES LOS NOMRBES los archivos y los guarda en la variblaes, asi como tambienlos directorios

readconteny():
"""Lee  el archivo y guarda el contenido del archivo en la varibale content, que se convierte En una lista o array donde cada indice tiene una linea de texto y/o un salto de linea"""
'''Abre el block de notas y guarda el contenido en la variable content, en memoria en pocas palabras, para luego en este bucle, infinito o indeterminado, al ingresar en cada linea'''

# COMENTARIOS APARTEA
