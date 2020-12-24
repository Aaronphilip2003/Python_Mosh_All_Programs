name=input("Enter your name(3-50characters only):")
length=len(name)
if length<3 or length>50 :
    print("ERROR!")
else:
    print("Name Looks Good!")