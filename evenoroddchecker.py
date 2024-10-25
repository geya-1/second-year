def check_even_odd(num):
    if num % 2 = 0:   # Mistake 1: Syntax error, should be '=='
        print(f"{num} is even")
    else
        print(num + " is odd")  # Mistake 2: Incorrect string concatenation with int
    return None  # Mistake 3: Unnecessary return value

# Test the function
check_even_odd(7)  # Mistake 4: No edge case for non-integer input
check_even_odd(-4)  # Mistake 5: Edge case: should handle negative numbers properly
