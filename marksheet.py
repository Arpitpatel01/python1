# name=input("enter the name")
# std=int(input("enter the stdy class"))
# mark=int(input("enter the mark"))
# if(mark>=70 ):
#     print("dict")
# elif(mark>65 and mark<70):
#     print("1st class")
# elif(mark>60 and mark<65):
#     print("2nd class")
# elif(mark>55 and mark<60):
#     print("3th class")
# else:
#     print("Fail")

x=["john","jenis","dev"]
name=input("enter the name" in x)
if(name==x):
    mark=input("enter the mark")
    if(mark>=70 ):
         print("dict")
    elif(mark>65 and mark<70):
         print("1st class")
    elif(mark>60 and mark<65):
         print("2nd class")
    elif(mark>55 and mark<60):
         print("3th class")
    else:
         print("Fail")
else:
    print("not valid class")
   