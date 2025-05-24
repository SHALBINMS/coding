def is_palindrome(num):
    num_str=str(num)
    
    return num_str==num_str[::-1] #reverse order 
    

num=input("enter the input")

if num.startswith("-"): #if input starts with "-" (eg: -121)
    num=num[1:] #splice to (eg: 121)


if is_palindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")