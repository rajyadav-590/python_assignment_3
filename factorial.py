#using loop
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact*i
        return fact    
#using recursion


# def factorial(num):
#     # Base case
#     if num == 0 or num == 1:
#         return 1
#     # Recursive case
#     else:
#         return num * factorial(num - 1)



if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        if user_input<0:
            print('negative values are not allowed.....')
        else:
            result = factorial(user_input)
            print(f"Factorial of {user_input} is: {result}")    
    except ValueError:
        print("Entered a wrong value, please enter only positive integer value..........")