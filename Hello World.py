# Hello, this is just a random coding video

# Print statment is used to print or get output from the machine (PC/Laptop).

print ("Hello world")

# As you can see this stament has been printed in output console

"""
Now let's just understand statments if i want to put this line here it will fail to execute the program
As you can see there is a syntax error show in the output console because of these lines 
these lines are not understandable by machine. Machine just understand the predefined syntax.
these lines are just random statment and are not understandable by machine
to have these lines in the code and at the same time we want our program to be exectued perfectly
we need to comment out these statements
"""
# or we can use # sign to comment out these statements and these will be avoided by the machine
# here you can see program is executed succesfully and comment out staements are avoided.
# Shortcut to comment out the uneccessary statements is ctrl + /

# now lets se how can we print 2 lines in python

# Method: 01

print ("This is first line ")
print ("This is second line")

# Method: 02

print("This is first line of code \nThis is second line of code")

# So as you can se this \(Forward slash) + n is a command for NEW LINE or write the rest of the statment on next line

# Moving to the next topic We are now gonna lear Variables

a = 10
b = 20
print (a)
print (b)

# or we can just put both together

print(a,b)

# As you can se the second method of printing both varriables value at the same time comes in 1 line
# For that we know we can use \n

print(a,"\n",b)

# But this second method is not a good practice.

# now let's just learn more about how a varriable stores avalue
# Varriable as name suggest can change it's value multiple times

a = "Daniyal" #Here a contains a string value

print (a)

a = 10 #Here a contains ainteger value

print(a)

a = 10.123456 #Here a contains a float value (Decimal value)

print (a)

a = 10-2j #Here a contains a complex number value (Having imaginary part (Iota))

print (a)

# So just lest check if our data types are being guided by python

a = "Daniyal" #Here a contains a string value

print (a,type(a))


a = 10 #Here a contains an integer value

print (a,type(a))

a = 10.123456 #Here a contains a float value (Decimal value)

print (a,type(a))

a = 10-2j #Here a contains a complex number value (Having imaginary part (Iota))

print (a,type(a))

# So as you can se first a was containing a string value and printed that but in next line i just putted an integer value
# As a is a varriable it just over write the new value on it instead of giving error
# So that's clear that code is executed line by line and as the new instruction is give it gives new value to a

# Now we are run some mathematical operation on varriables and stor their value in new varriables

a = 10
print("value of a =", a)

b = 3git 0
print("value of b =",b)

# now there are 2 methods

# Method 01

print("Addition of a and b =",a+b)

# Method 02

c= a+b
print("value of c =", c)

# Same goes for Subtraction, Multiplication and Division

c= a-b
print("value of c =", c)
c= a*b #For multiplication "*"
print("value of c =", c)
c= a/b #For division "/(Back slash)"
print("value of c =", c)

# Now We I'll be learning some other operators like equals, not equals, greater than, less than, and not equals.

a = 10
print (a)

b = 20
print(b)



