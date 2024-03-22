def is_palindrome_integer(x):
    
    str_x = str(x)
    
    return str_x == str_x[::-1]

number = int(input("Enter an integer to check if it's a palindrome: "))
result = is_palindrome_integer(number)
print("Is the number a palindrome?", result)
