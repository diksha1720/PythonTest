"""
This is a python code for getting a string and making some alterations to it
"""
print("Enter the sring\n")

x=input()
print("The string is "+x)
print("In Upper case "+x.upper())
print("In lower case "+x.lower())
print("Character "+x[1])
print("Range of charater "+x[2:5]) #2 and 5 not inlucded 
print("To remove white space from front and end  "+x.strip()) #removes white space at beginning and end
a=len(x)
print("Length ="+str(a)) #since length is an int, it has to be typecasted to string to print!
print("To replace "+x.replace('H','K'))
print("To slipt the string based on some character"+str(x.split(','))) #returns ['Hello','World'], has to be typecasted to str
