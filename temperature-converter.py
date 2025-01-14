def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  

def celsius_to_kelvin(celsius):
    return celsius + 273

def kelvin_to_celsius(kelvin):
    return kelvin - 273 


opcao = input(''' Menu: 
              
    (1) - C to F
    (2) - F to C
    (3) - C to K
    (4) - K to C
    (5) - Exit 
        
''')    

while True:
    match opcao:
        case '1':
            celsius = float(input('Temperature in celsius: '))
            print(f'{celsius}°C equals {celsius_to_fahrenheit(celsius)}°F')

        case '2':
            fahrenheit = float(input('Temperature in fahrenheit: '))
            print(f'{fahrenheit}°F equals {fahrenheit_to_celsius(fahrenheit)}°C' )

        case '3':
            celsius = float(input('Temperature in celsius: '))
            print(f'{celsius}°C equals {celsius_to_kelvin(celsius)}K')

        case '4':
            kelvin = float(input('Temperature in kelvin: '))
            print(f'{kelvin}K equals {kelvin_to_celsius(kelvin)}°C')

        case '5':
            print('You chose to leave ')
            break

        case _:
            print('Please, choose an avaliable option. ')