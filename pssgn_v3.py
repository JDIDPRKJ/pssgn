#https://github.com/JDIDPRKJ/
import random
import json
import os

long = '0'
num = '0'
characters = ''

try:
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')
        if(os.path.isfile('config.json')):
            with open('config.json', 'r') as dicc:
                diccJson = json.load(dicc)
                if(os.path.isfile(diccJson['DICC'])):
                    with open(diccJson['DICC'], 'r') as char:
                        characters = char.read()
                else:
                    print('No se encuentra el archivo en la ruta guardada. ' + diccJson['DICC'])
        else:
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()'
        print('     ____.________  .___ \n    |    |\______ \ |   |\n    |    | |    |  \|   |\n/\__|    | |    `   \   |\n\________|/_______  /___|\n                  \/ v3 pssgn\n')
        command = str(input('Comando >> '))
        command = command.split()
        if(command[0] == 'cls' or command[0] == 'clear'):
            try:
                os.system('cls')
            except:
                os.system('clear')
        elif(command[0] == 'dicc'):
            if(len(command) == 1):
                print('Necesitas especificar la ruta de el diccionario.')
            else:
                if(os.path.isfile(command[1])):
                    with open(command[1]) as dicc:
                        characters = dicc.read()
                    try:
                        if(command[2] == '-s' or command[2] == '--save'):
                            dataJson = { "DICC":command[1] }
                            with open('config.json', 'w') as configJson:
                                json.dump(dataJson, configJson)
                            print('Se obtuvo correctamente el diccionario y se guardo la direccion de el diccionario')
                    except:
                        print('Se obtuvo correctamente el diccionario, para guardar el diccionario como principal escriba dicc [ruta] -s')
                else:
                    print('No se encuentra el archivo en la ruta seleccionada.')
        elif(command[0] == 'log'):
            if(len(command) == 1):
                with open('log_pssgn.txt', 'r') as log:
                    print('\n' + log.read())
                input('Precione enter para continuar [se borrara la consola]')
            else:
                try:
                    if(command[1] == '-c' or command[1] == '--clear' or command[1] == 'clear' or command[1] == 'c'):
                        with open('log_pssgn.txt', 'w') as log:
                            log.write('')
                except:
                    pass
        elif(command[0] == 'pass'):
            if(len(command) == 1):
                print('Necesitas ingresar una longitud')
            elif not(command[1].isnumeric()):
                print('Ingrese un valor valido en la longitud')
            else:
                if(int(command[1]) < 0):
                    print('Debes ingresar un numero mayor o igual a 1')
                else:
                    try:
                        num = int(command[2])
                    except:
                        num = 1
                    if not(command[1].isnumeric()):
                        print('Necesitas ingresar un numero valido')
                    else:
                        long = int(command[1])
                        for _ in range(num):
                            password = ''
                            for _ in range(long):
                                char = random.choice(characters)
                                password = password + char
                            print(password)
                            try:
                                if(command[3] == '-s' or command[3] == '--save'):
                                    with open('log_pssgn.txt', 'a') as log:
                                        log.write(password + '\n')
                            except:
                                pass
                        input('Precione enter para continuar [se borrara la consola]')
                        try:
                            os.system('cls')
                        except:
                            os.system('clear')
except KeyboardInterrupt:
    try:
        os.system('cls')
    except:
        os.system('clear')
    print('Interrupcion de el teclado')
