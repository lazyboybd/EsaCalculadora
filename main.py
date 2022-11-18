import math


def calculate():
    operation = input('''
Escolher a operaçao matematica:
+ Adiçao
- subtraçao
* multiplicaçao
/ divisao
** potencia
r raiz quadrada
% Percentagem
''')

    if operation == '**':
        print("base e expoente:")
        base = int(input("Base: "))
        expoente = int(input("Expoente: "))
        potencia = 1
        for count in range(expoente):
            potencia *= base
            count += 1

        print(base, "^", expoente, "=", potencia)

    if operation == 'r':
        num = float(input("Inserir um numero:\n"))
        raiz = math.sqrt(num)
        print(f'\nA raiz quadrada de {num} é {raiz}\n')

    if operation == '%':
        print("percentagem de valor:")
        perc = float(input('Percentagem: '))
        value = float(input('Valor: '))
        result = (value * perc)/100
        print(f'{perc} % de {value} é = {result}')


    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        number1 = float(input('Inserir o primeiro numero: '))
        number2 = float(input('Inserir o segundo numero: '))

        if operation == '+':
            print('{} + {} = '.format(number1, number2))
            print(number1 + number2)

        elif operation == '-':
            print('{} - {} = '.format(number1, number2))
            print(number1 - number2)

        elif operation == '*':
            print('{} * {} = '.format(number1, number2))
            print(number1 * number2)

        elif operation == '/':
            print('{} / {} = '.format(number1, number2))
            print(number1 / number2)


        else:
            print('Mete o sinal primeiro.')

    again()


def again():
    calc_again = input('''
Queres mesmo fazer de novo??
S para sim e N para nao.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Cya.')
    else:
        again()

calculate()