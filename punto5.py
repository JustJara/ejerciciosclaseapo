#. Crear una función que convierta grados Fahrenheit a grados Celsius.

def convertidor_fahrenheit_a_celcius(temp_fahrenheit):
    temp_celcius = (temp_fahrenheit-32) * 5/9
    return temp_celcius

print(convertidor_fahrenheit_a_celcius(32))