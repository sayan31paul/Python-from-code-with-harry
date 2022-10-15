print(type(36.7))

#Type_Casting- Converting from one datatype to another is known  as type casting.
var1="82"
var2="56"
print(var1+var2) #string concatenation
print(int(var1)+int(var2))

#str() :- Converts a datatype to string
#float():- Converts a datatype to float
#int():- Converts a datatype to int

print(10* "Hello_World ")
print(10* "Hello_World\n")

#taking input from user
inpnum=input("Enter a number: ") # input() always takes input in string format. So type-casting is necessary.
inpnum=int(inpnum)
print(type(inpnum))