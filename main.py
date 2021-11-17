from os import replace

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
            content.pop(i)
    except:
        print("Ya termino")
        break


print(content)
j = 0
text = ""
while True:
    try:
        if len(content) >= j:
            text = text + content[j].replace(' ', '_').append('.md')
            j = j+1
    except IndexError:
        print("ya termino")
        break
print(text)
new_text = open('Z:\\PROGRAMACION\\python\\app_console_formating_test\\new.txt', 'w')
new_text.write(text)
new_text.close()
