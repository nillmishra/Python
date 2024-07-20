story = "once upon a time there was a coder named nill who used to code in github"
#string function
print(len(story))
print(story.endswith("sdqhdf"))
print(story.count("a"))
print(story.count("wa"))
print(story.capitalize())#first word ko capitalize kar k deta hai
print(story.find("nill"))
print(story.find("nili"))
print(story.find("once"))
print(story.replace("nill", "Nill Mishra"))

apple = '''He said,
hi Nill
hey i am good
'''

print(apple)


print("Lets use a for loop\n")
for cshow in apple:
    print(cshow)