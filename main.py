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
        potencia()

    if operation == 'r':
        raiz()

    if operation == '%':
        percentagem()

    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        number1 = float(input('Inserir o primeiro numero: '))
        number2 = float(input('Inserir o segundo numero: '))

        if operation == '+':
            soma(number1,number2)

        elif operation == '-':
            sub(number1,number2)

        elif operation == '*':
            mult(number1,number2)

        elif operation == '/':
            div(number1,number2)

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


def potencia():
    print("base e expoente:")
    base = int(input("Base: "))
    expo = int(input("Expoente: "))
    potenciaResult = 1
    for count in range(expo):
        potenciaResult *= base
        count += 1

    print(base, "^", expo, "=", potenciaResult)


def raiz():
    num = float(input("Inserir um numero:\n"))
    if num > 0:
        raiz = math.sqrt(num)
        print(f'\nA raiz quadrada de {num} é {raiz}\n')
    else:
        print('Nao pode ter numeros negativos')


def percentagem():
    print("percentagem de valor:")
    perc = float(input('Percentagem: '))
    value = float(input('Valor: '))
    result = (value * perc) / 100
    print(f'{perc} % de {value} é = {result}')


def soma(x, y):
    print('{} + {} = '.format(x, y))
    print(x + y)


def sub(x, y):
    print('{} - {} = '.format(x, y))
    print(x - y)


def mult(x, y):
    print('{} * {} = '.format(x, y))
    print(x * y)


def div(x, y):
    print('{} / {} = '.format(x, y))
    print(x / y)


calculate()
