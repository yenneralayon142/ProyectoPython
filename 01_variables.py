#Variable #

my_string_variable = "My string variable"
print(my_string_variable)
my_int_variable = 5
print(my_int_variable)
my_bool_variable = True
print(my_bool_variable)

#Concatenar Variables #
print(my_string_variable,my_int_variable,my_bool_variable)

#Parsear un valor #
my_int_variable = str (my_int_variable)
print (my_int_variable)
print(type(my_int_variable))

#Contar caracteres #
print(len(my_string_variable))

#Variables en una sola linea #
name,surname,alias,age = 'Yenner', 'Alayon' , 'flaco' , 20
print('Me llamo',name,surname,'me dicen',alias, "y tengo",age) 

first_name = input('¿Cual es su nombre?')
age = input('How are you')

print(first_name)
print (age)