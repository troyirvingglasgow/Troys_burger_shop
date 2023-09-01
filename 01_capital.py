def capitalize_name(name):
    if not name:
        return ""

    # Convert the first character to uppercase and the rest to lowercase
    capitalized = name[0].upper() + name[1:].lower()
    return capitalized


input_name = input("Please enter the name you would like your order under:")
name = capitalize_name(input_name)
print("Thanks for ordering with us {}, you're final order is:".format(name))