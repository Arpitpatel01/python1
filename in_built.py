#capitalize()
txt="hello, and welcome to my world"
x=txt.capitalize()
print(x)

#casefold()
txt="hello, and welcome to my world"
x=txt.casefold()
print(x)

#center()
txt="hello"
x=txt.center(20)
print(x)

#count()
txt="hello world, and welcome to my world"
x=txt.count("world")
print(x)

#encode()
txt="hello, and welcome to my world"
y=txt.encode()
print(y)

#endswith()
txt="hello, and welcome to my world."
a=txt.endswith(".")
print(a)

#expandtabs()
txt="h\te\tl\tl\to"
b=txt.expandtabs(2)
print(b)

#find()
txt="hello, and welcome to my world"
c=txt.find("welcome")
print(c)

#format()
# txt="for only {prince:.2f} dollars!"
# print(txt.format(print=49))

#index()
txt="hello, and welcome to my world"
x=txt.index("welcome")
print(x)

#islower
txt="hello, and welcome to my world"
x=txt.islower()
print(x)

#isnumenic
txt="47845656"
x=txt.isnumeric()
print(x)

#isprintable
txt="hello! are you #1?"
x=txt.isprintable()
print(x)

#isspace
txt=" "
x=txt.isspace()
print(x)

#isupper
txt="HELLO WORLD"
x=txt.isupper()
print(x)

#join
mytuple=("john","peter","vicky")
x="#".join(mytuple)
print(x)

#ltrip()
txt=" banana     "
x=txt.lstrip()
print("of all fruits",x,"is my favorite")

#replace()
txt="hello, and welcome to my world"
x=txt.replace("world","gujarat")
print(x)

#lower()
txt="HELLO WORLD GUJARAT"
u=txt.lower()
print(u)

#upper()
txt="hello, and welcome to my world"
x=txt.upper()
print(x)

#compare string
str1="hello, and welcome to my world"
str2="hello, and welcome to my world"
result= str1 == str2
print(result)