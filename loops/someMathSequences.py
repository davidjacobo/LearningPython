def listFib(limit):
    fList = [1]
    a = 0
    b = 1
    while b <= limit:
        c = a+b
        a = b
        b = c
        fList.append(c)
    return fList

def linearRangeSum(lst,x,y):
    ans = 0

    #Linear time answer
    for i in range(x,y):
        ans = ans + lst[i]

    return ans

def fillArrayWithSequence(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


n = int(input("Array len"))

seqList = fillArrayWithSequence(n)
print("The sum of the values:")
print(seqList)
print("is:")
print(linearRangeSum(seqList, 0, n))

seqList = listFib(n)
print("Printing the terms smaller or equals than {} in the Fibonacci series".format(n))
print(seqList)
