file_text = open('Z:\\PROGRAMACION\\python\\app_console_formating_test\\texto.txt', 'r')
content = file_text.readlines()
file_text.close()

print(content, type(content), len(content))
i = len(content)-1
while  True:
    try:
        if content[i] != '\n' and i <= len(content):
            i = i-1
        else:
            print("aqui hay salto te linea, se va a borrar esta linea", len(content))
            content.pop(i)
            print(len(content))
    except:
        print("Ya termino")
        break

print(content)

new_text = open('Z:\\PROGRAMACION\\python\\app_console_formating_test\\new.txt', 'w')
new_text.write(content)
new_text.close()
