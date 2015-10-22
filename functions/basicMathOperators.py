def suma(valA,valB):
    #Sum 2 values or report is not possible if the
    #given data is not numeric
    try:
        valC = valA+valB
    except Exception as e:
        valC = 0
        print("Cannot sum this ",e)
    return valC

def mult(valA, valB):
    #Multiply 2 numbers or report there is an error
    try:
        valC = valA*valB;
    except Exception as e:
        valC = 0
        print("Cannot multiply this ",e)
    return valC

def expo(valA, valB):
    #pow valA ^ valB
    try:
        valC = valA**valB
    except Exception as e:
        valC = 0
        print("Cannot pow this stuff ",e)
    return valC
