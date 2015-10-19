#Example of a person data which CANNOT be modified
coolTuple = ("Armando","'el desmadre'","Lopez",27)

#Building the full name on a single variable
fullName = coolTuple[0] + " " + coolTuple[1] + " " + coolTuple[2]

#Cannot modify the contents u,u
#coolTuple[0] = 12

#Format the message and print
output = "{} is {} years old".format(fullName, coolTuple[3])
print(output)
