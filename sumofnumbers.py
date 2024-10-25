def sum_of_list(lst):
    total = 0
    for num in lst:
        total = total + n  # Mistake 1: Incorrect variable name 'n'
    return Total  # Mistake 2: Case-sensitive typo 'Total' instead of 'total'

# Test the function
print(sum_of_list([1, 2, '3', 4]))  # Mistake 3: Fails for non-integer items in list
print(sum_of_list([1, 2, 3, 4, 5]))  # Mistake 4: No error checking for empty lists
print(sum_of_list([]))  # Mistake 5: Empty list case returns None instead of 0
