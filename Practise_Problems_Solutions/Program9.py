import re
def is_valid(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True


a = input("Enter comma-separated passwords: ").split(',')
valid_password = [password for password in a if is_valid(password)]

print(','.join(valid_password))
