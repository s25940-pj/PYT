def generate_password(length):
    import random
    import string

    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    return password


length = int(input("Wpisz długość hasła: "))
print(generate_password(length))
