mystr="harry is a good boy"
print(mystr)

#indexing in string
print(mystr[4]) #Indexing in python starts from zero
print(mystr[5])

#slicing
print(mystr[0:8])

#finding the length of string
print(len(mystr))

#slicing by skipping characters
print(mystr[0:10:2])

print(mystr.isalnum()) #"""al-alphabet, num-numeric. If spaces comes in between then it will not be considered as alphabet"""
"""isalnum() means it should contain either alphabet or numbers or both but it should not contain spaces."""
print(("Harryisagoodboy").isalnum())

print(mystr.endswith("boy"))
print(mystr.endswith("good boy"))

print(mystr.capitalize()) #capitalizes the first letter.

print(mystr.find("is")) #gives the index where "is" starts

print(mystr.upper()) #.upper() converts entire string into upper case.

print(mystr.replace("is","Are")) #replaces a part of a string with another string