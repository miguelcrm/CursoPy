# Calculadora com While
''''''
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Operador:')

    num1_float = 0
    num2_float = 0
    numeros_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None


    if numeros_validos is None:
        print('Um ou ambos os números são inválidos!')
        continue

    operadores = '+', '-', '*', '/'
    operador_vazio = ''
    
    if operador == operador_vazio:
        print('Digite um operador!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    if operador not in operadores:
        print('Digite um operador válido!')
        continue

    

    soma = num1_float + num2_float

    subtracao = num1_float - num2_float

    multiplicacao = num1_float * num2_float

    divisao = num1_float / num2_float

    if operador == operadores[0]:
        print(f'A soma dos números {num1_float} + {num2_float} =', soma)

    if operador == operadores[1]:
        print(f'A subtração dos números {num1_float} - {num2_float} =', subtracao)
    
    if operador == operadores[2]:
        print(f'A multiplicação dos números {num1_float} * {num2_float} =', multiplicacao)
    
    if operador == operadores[3]:
        print(f'A divisão dos números {num1_float} / {num2_float} =', divisao)
    

    sair = input('Você deseja [s]air? ').lower().startswith('s')

    if sair is True:
        break