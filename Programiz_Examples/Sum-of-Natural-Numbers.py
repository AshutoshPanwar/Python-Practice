# Python Program to Find the Sum of Natural Numbers

# Using for loop
def sum_using_loop(num):
    result = 0
    for i in range(num + 1):
        result += i
    return result

# Using Formula
def sum_using_formula(num):
    return num * (num + 1) // 2

# Using sum with range
def sum_using_sum_function(num):
    return sum(range(1, num+1))

# Using Recursion
def sum_using_recursion(num):
    if num == 0:
        return 0
    else:
        return num + sum_using_recursion(num - 1)

n = int(input("Enter the number: "))
result = sum_using_loop(n)
print(f"The sum of natural numbers up to {n} using a loop is: {result}")

result = sum_using_formula(n)
print(f"The sum of natural numbers up to {n} using the formula is: {result}")

result = sum_using_sum_function(n)
print(f"The sum of natural numbers up to {n} using the sum function is: {result}")

result = sum_using_recursion(n)
print(f"The sum of natural numbers up to {n} using recursion is: {result}")