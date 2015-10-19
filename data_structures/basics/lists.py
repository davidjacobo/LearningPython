coolList = []

coolList.append(1)

coolList.append("adding words? wtf!")

coolList.append(2.5);

#Print all the contents
print(coolList)

#Partial print of the elements
step = 2
print(coolList[0:3:step])

#Basic arithmetic using the list' values
coolList[0] += 100

coolList[-1] *= 2.0

#Pick some elements from the list to print
output = "message: {0:s} and value: {1:d}".format(coolList[1], coolList[0])
print(output)
