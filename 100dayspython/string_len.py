#strings are immutable
f= "mango!!!!!  !!!! mfewd"
len = len(f)
print(len)
print(f.upper())
print(f.lower())
print(f.rstrip("!"))
print(f.replace("mango", "banana"))
print(f.split(" "))
blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
# print(len(str1))
# print(len(str1.center(50)))
# print(len(str1) + (50 - len(str1)))
print(f.count("go"))

print(str1.endswith("!!!"))

str2 = "He's name is dan, HE is an honest man."
print(str2.find("is"))
print(str2.index("HE"))

str3 ="WelcomeTOConsol00e"
print(str3.isalnum())
print(str3.isalpha())
print(str3.islower())

str4 = "We wish you a Merry Chritmas\n"
print(str4.isprintable())


str1 = "     " #using spacebar
print(str1.isspace())

str1 = "    " #using tab
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpretd Language"
print(str1.startswith("Python"))


str1 = "Python is Interpreted Language"
print(str1.swapcase())

str1 = "HE's name is Dan. Dan is a honest man."
print(str1.title())