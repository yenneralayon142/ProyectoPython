"""
my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + "" + my_other_string)

my_new_line_string = "Este es un String\n con salto de linea"
print(my_new_line_string)

my_tab_string = "Este es un string con tabulacion"
print(my_new_line_string)

# Invertir cadena

cadena = "esto es una cadena"
result = ""

result = cadena[::-1]
print(result)


#Contar un  caracter

cadena = "LLLLLss"
letra = 'L'
count = 0

for i in cadena:
    if i == letra:
        count += 1

print(count) 


# Distancia de Hamming

cadena1 = "esto es futbol"
cadena2 = "esto es futdolzxcsd"
count = 0

if len(cadena1) != len(cadena2):
    raise Exception("Las longitudes son distintas")

for i in range(len(cadena1)):
    if cadena1[i] != cadena2[i]:
        count += 1

print(count)


#Contar palabras

cadena = "Esto es futbol"

palabras = cadena.split()

count_Palabras = len(palabras)

print(count_Palabras)
 """


cadena = "danna es sapa"
result = ""

result = cadena[::-1]

print(result)

