def celcius_to_fahrenheit(celcius):
    return celcius * 9 / 5 + 32


celcius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = celcius_to_fahrenheit(celcius)
print("Temperatura w stopniach Fahrenheita: ", fahrenheit)
