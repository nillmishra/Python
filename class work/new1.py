default_order = "{} {} {}" . format('TOday', 'is', 'sunday')
print(default_order)
default_order = "{1} {0} {2}" . format('is', 'Today', 'sunday')
print(default_order)
key_order = "{t} {i} {s}" . format (i = 'is', t = 'today', s = 'sunday')
print(key_order)
print("Binary representation of {0} is {0:b} " . format(20))
print("Exponent representation of {0} is {0:e} " . format(1200.0))
print("One third representation of {0} is {0:3f} " . format(1/3))

print("gooD morning to alL" . lower())
print("Good Morning tO alL" . upper())
print("gooD morning tO all" . find("tO"))
print("Good morning to all". replace("all", "everyone"))