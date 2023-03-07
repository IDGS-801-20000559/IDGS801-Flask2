"""
file = open('alumno.txt', 'r')

nombres = file.readlines()
print(nombres)
file.close()

for nombre in nombres:
   print(nombre, end='')
"""
# Parametros a agregar en el metodo open
# a = adicionar
# w = write
# r = read

file = open('alumnos2.txt', "a")
file.write("\nHola Gerson!")
file.close()

""""
# Para ingresar más datos en un txt
file = open('alumno.txt', 'a')
file.write("Azul Blue\n")
file.write("Amarillo Yellow\n")
file.close()


def buscar(archivo, parametro):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            datos = linea.split()
            if datos[0] == parametro:
                return linea.strip()
            elif datos[1] == parametro:
                return linea.strip()

color = buscar('alumno.txt', 'Blue')

if(color != None):
    color = color.split()
    colorEspaniol = color[0]
    colorEnIngles = color[1]
    print(colorEspaniol+" en inglés es "+colorEnIngles)
else:
    print("No se encontraron registros")
"""