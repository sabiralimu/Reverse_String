# Input a string
user_input = input("Enter a string: ")

# Reverse the string with builtin functions
#reversed_string = user_input[::-1]

## Reverse the string with for loops

# Initialize an empty string for the reversed input
reversed_string = ""

# Loop through each character in the input string
for char in user_input:
    reversed_string = char + reversed_string

# Output the reversed string
print("Reversed String:", reversed_string)