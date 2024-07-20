x = 56
# x is the variable to match
match x :
    #if x is 0
    case 0:
        print("X is Zero")
    case 4 if x%2 == 0:
        print("x % 2 == 0 and case is 4")
    
    case _ if x<10:
        print("x is < 10")

    case _:
        print(x)