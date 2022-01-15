#https://github.com/JDIDPRKJ/
import os
import random

print('     ____.________  .___ \n    |    |\______ \ |   |\n    |    | |    |  \|   |\n/\__|    | |    `   \   |\n\________|/_______  /___|\n                  \/     \n')

try:
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()'
    while True:
        password_long = int(input("Longitud >> "))
        password_nume = int(input("Repeticiones >> "))
        for _ in range(password_nume):
            password = ''
            for _ in range(password_long):
                password_char = random.choice(characters)
                password = password + password_char
            print(password)
        input('\nPrecione una tecla para continuar')
except KeyboardInterrupt:
    os.system('cls')
    print('Ejecucion interrumpida')