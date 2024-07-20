#creating list
heros = ["saktiman", "nagraj", "shakal", "baalveer"]
print(heros)

#accesing list
print(heros[3])

#append function list
heros.append("yoman")
print(heros)

#inserting new element using 
heros.insert(3, "krish")
print(heros)

#soting acording to alphabet
heros.sort()
print(heros)

#updaiting
heros.append("A")
print(heros)


#updating last index
heros[-1] = "flyingjat"

numbers = [1,2,3,4,5,6,7]
print(numbers)
heros.append(numbers)
print(heros)

heros.extend(numbers)
print(heros)

heros.pop(4)
print (heros)

heros.reverse()

print('bonbsingh' in heros)
print(heros)