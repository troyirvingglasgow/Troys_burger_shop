
def format_name(name):
    formatted_name = name.capitalize()
    return formatted_name

# Get input from the user
user_input = input("Enter a name: ")

# Format the name using the function
formatted_result = format_name(user_input)

# Print the formatted result
print("Your name:", formatted_result)

def capitalize_name(name):
    if not name:
        return ""

    # Convert the first character to uppercase and the rest to lowercase
    capitalized = name[0].upper() + name[1:].lower()
    return capitalized

# Test cases
input_name = input("Enter a name: ")
capitalized_result = capitalize_name(input_name)
print("Capitalized:", capitalized_result)