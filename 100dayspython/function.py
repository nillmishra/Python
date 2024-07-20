# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print(gmean)



# gmean2 = (c*d)/(c+d)
# print(gmean2) 

def calculationGmaen(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if (a>b):
        print("first number is greater")
    else:
        print("Second naumber is greater")

def isLesser(a,b):
    pass

a = 9 
b = 8
calculationGmaen(a, b)
isGreater(a,b)

c = 8
d = 7
calculationGmaen(c, d)
isGreater(c,d)