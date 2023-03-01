def sareizinat_ar_divi(x):
    return x * 2

print(sareizinat_ar_divi(5))

def say_hello_to(name):
    print(f"Labdien {name}, priecīgus svētkus!")

say_hello_to('Elizabete')
say_hello_to('Oskars')
say_hello_to('Elvin')
say_hello_to('Anna')



def say_something():
    print('Something')

say_something()


def sum_of_two_numbers(number1, number2):
    return number1 + number2

print(sum_of_two_numbers(4, 5))


# UZDEVUMS 1
# Definē funkciju kas pārveidos Fahrenheit uz Celsius

def convert_to_celsius(temp_f):
    return (temp_f - 32) * 5/9

user_value = float(input("Temperature in F: "))
print(convert_to_celsius(user_value))

