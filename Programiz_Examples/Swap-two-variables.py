# Adding two numbers using temp variable

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

# Swaping varibles
temp = x
x = y
y = temp

print("Value of x and y after swaping are {}, {}".format(x,y))

#############################
# Without using temp variable
x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

x, y = y, x

print("Value of x and y after swaping are {}, {}".format(x,y))

##############################
# Using arithmetic operators
print("using Additon and Subtraction")

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

x = x + y
y = x - y
x = x - y
print("Value of x and y after swaping are {}, {}".format(x,y))

###############################
print("using Multiplication and Division")

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

x = x * y
y = x / y
x = x / y
print("Value of x and y after swaping are {}, {}".format(int(x),int(y)))

#################################
print("using XOR")

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

x = x ^ y
y = x ^ y
x = x ^ y
print("Value of x and y after swaping are {}, {}".format(x,y))