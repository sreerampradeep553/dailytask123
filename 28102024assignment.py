# ASSIGNMENT

#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

def greet(name):
    print(f"hello,{name}!")

greet(input("enter the name:"))


# 2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.

def add_numbers(a,b):
    return a+b

print(add_numbers(10,34))


#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(n):
    return n%2==0

print(is_even(9))
print(is_even(19))
print(is_even(10))
print(is_even(15))
print(is_even(16))

#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
 
def factorial():
    n = int(input("Enter a positive integer: "))
    result = 1 
    for i in range(1,n+1):
        result *= i 
    print("Factorial:",result) 
factorial()

 # 5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.

def find_max(a,b,c):
   return max(a,b,c)

print(find_max(10,20,30))
print(find_max(11,15,20))
print(find_max(15,10,25))

# 6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

print(count_vowels(input("enter the string:")))
print(count_vowels(input("enter the string:")))
print(count_vowels(input("enter the string:")))

# 7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True


print(is_prime(int(input("enter the number:"))))
print(is_prime(int(input("enter the number:"))))
print(is_prime(int(input("enter the number:"))))


# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(n):
    if n<= 1:
        return n
    else:
        return n+recursive_sum(n-1)
    
print(recursive_sum(5))
print(recursive_sum(25))
print(recursive_sum(15))
print(recursive_sum(22))

# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def calculator ():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter an operator(+,-,*,/): ")
    if operator == "+":
        print("Result:", a+b)
    elif operator == "-":
        print("Result:", a-b)
    elif operator == "*":
        print("Result:", a*b)
    elif operator == "/":
        print("Result:", a/b)
    else:
        print("Division by zero is not allowed.")
calculator()


# 10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists


def common_elements():
    list1 = input("Enter the first line of element separated by spaces: ").split()
    list2 = input("Enter the second line of element separated by spaces: ").split()
    common_elements = list(set(list1) & set(list2))
    print("Common Elements: ",common_elements)
common_elements()


# 11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string():
    string = input("Enter a string: ")
    print("Reversed String: ",string[::-1])
reverse_string()

# 12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.


def sort_dict_by_value():
    d = {}
    n = int(input("Enter items in dictionary: "))
    for i in range(n):
        key = input("Enter key:")
        value = input("enter value:")
        d[key] = value 
    sorted_dict = sorted(d.items(),key = lambda item: item[1])
    print("Sorted Dictionary by Value:",sorted_dict)
sort_dict_by_value()