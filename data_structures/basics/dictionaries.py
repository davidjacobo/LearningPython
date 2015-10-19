#Define a dictionary
coolDic = dict()

#Add a few People and their telephone numbers
coolDic["Prudencio"] = "3312349876"
coolDic["Ramiro"] = "3398982342"

print(coolDic)

#Well Prudencio changed his cell phone
coolDic["Prudencio"] = "0101010101"

print(coolDic)

#Ramiro really needs to get outta the database
del coolDic["Ramiro"]

print(coolDic)

#Adding a pair with a different format
coolDic[5] = 0.1

print(coolDic)
