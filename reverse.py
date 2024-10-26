def reverse_string(s):
    # Check if the input is a string
    if not isinstance(s, str):
        return "Input must be a string"
    
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Add the current character to the front

    return reversed_str  # Return the correct variable

# Test the function#
print(reverse_string("Hacktoberfest")) 
print(reverse_string(12345))             # Expected output: "Input must be a string"
print(reverse_string(""))                 # Expected output: ""
