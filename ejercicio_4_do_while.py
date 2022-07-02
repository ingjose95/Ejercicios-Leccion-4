numero_ganador = 11

while True:

    su_numero = input('Ingrese un numero: ')

    if int(su_numero) == numero_ganador:
        print('Ha sido el ganador.')

        break;

    else:

        print('Usted ha perdido. Lo siento')

        break;