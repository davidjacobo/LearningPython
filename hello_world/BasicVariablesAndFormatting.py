thisIsAnInteger = 12
thisIsAFloat = 0.5
thisIsAString = "Yo no me llamo Javier!"

#Basic operations with numbers
edad = 27
edad+= 1

#Basic concatenation
nombre = "Armando"
alias = " 'el desmadre' "
apellido = "Lopez"

nombreCompleto = nombre + alias + apellido

'''
Basic string formating, %s and %d introduce placeholders
for the variables to be inserted
'''
output = "%s is %d years old"%(nombreCompleto, edad)
output2 = "{0:s} is {1:d} years old".format(nombreCompleto, edad)

#Both print's should show the same output
print(output)
print(output2)
