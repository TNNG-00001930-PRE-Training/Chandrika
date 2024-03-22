def string_operations():
    #1String concatenation
    str1 = "Hello"
    str2 = "World"
    conc_str = str1 + " " + str2
    print("Concatenated string:", conc_str)
    #2String slicing
    s = "Tammineni Chandrika"
    sliced_str = s[10:20]  # Slicing from index 7 to 17
    print("Sliced string:", sliced_str)
    #3String formatting
    name = "Chandrika"
    age = 21
    formatted_str = f"My name is {name} and I am {age} years old."
    print("Formatted string:", formatted_str)
    #4String manipulation methods
    s = " Tammineni Chandrika "
    upper_str = s.upper()
    lower_str = s.lower()
    stripped_str = s.strip()
    replaced_str = s.replace("Tammineni", "T")

    print("Uppercase:", upper_str)
    print("Lowercase:", lower_str)
    print("Stripped:", stripped_str)
    print("Replaced:", replaced_str)

string_operations()
