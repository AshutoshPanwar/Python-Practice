# Add two numbers

num1 = 1.1
num2 = 42.2

# Add two numbers and store to a variable
result = num1 + num2

# Display the Output
print("The Sum of {} and {} is {}".format(num1, num2, result))



################################
#Add Two Numbers With User Input

# Store two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second numebr: ")

# Add two numebrs
sum = float(num1) + float(num2)

print("The Sum of {} and {} is {}".format(num1, num2, sum))

###############################
# Adding without using any variables

print("The sum of %.1f" %(float(input("Enter first number: ")) + (float(input("Enter second number: ")))))