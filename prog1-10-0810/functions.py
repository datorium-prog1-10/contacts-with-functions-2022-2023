def sareizinat_ar_divi(x):
    return 2 * x

def say_hello_to(salutation, name):
    print(f"{salutation} {name}!")

say_hello_to('Labvakar', 'Elizabete')

# UZDEVUMS 1
# Definē funkciju kas pārveidos Fahrenheit uz Celsius

def f_to_c(temp_f):    
    return (temp_f - 32) * (5/9)

#user_input = float(input('Enter tempreratur in Farhenheit: '))
#print(f_to_c(user_input))

# Funkcija pieņem 2 vērtības:
# (1) temperatūra 
# (2) skala
# funkcija atgiež temperatūras vērtību otrajā skalā

def convert_temperature(temperature, unit):
    if unit == 'C':
        fahrenheit = temperature * 9 / 5 + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (temperature - 32) * 5 / 9
        return celsius

print(convert_temperature(90, 'F'))

