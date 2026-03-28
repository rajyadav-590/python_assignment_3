import math
try:
    
    user_input = float(input("Enter a number: "))
    if user_input<=0:
        print("Please enter a number greater than 0 for log and square root")
    else:    
        square_root = math.sqrt(user_input)
        logarithm = math.log(user_input)
        sine = math.sin(user_input)
        print(f"Square root: {square_root}")
        print(f"Logarithm: {logarithm}")
        print(f"Sine: {sine}")
except ValueError :
    print("wrong input....")