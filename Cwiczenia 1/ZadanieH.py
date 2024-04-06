def calculator():
    operand = input("Podaj działanie: ")
    first_number = int(input("Podaj pierwszą liczbę: "))
    second_number = int(input("Podaj drugą liczbę: "))
    if operand == "+":
        return first_number + second_number
    elif operand == "-":
        return first_number - second_number
    elif operand == "*":
        return first_number * second_number
    elif operand == "/":
        return first_number / second_number
    else:
        return "Nieprawidłowe działanie"


print(calculator())
