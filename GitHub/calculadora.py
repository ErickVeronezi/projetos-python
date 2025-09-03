#CALCULADORA EM PY

while True:
    operador = input(
        'Soma [+]  Divisão [/]  Multiplicação [*]  Subtração [-]\n'
        '============= PARA SAIR DIGITE [S] =============\n'
        'Escolha: '
    ).strip().lower()

    ## OPERAÇÃO PARA SAIR
    if operador.startswith('s'):
        print('Saindo...')
        break

    operadores_permitidos = '+-/*'
    if (len(operador) != 1) or (operador not in operadores_permitidos):
        print('Operador inválido. Tente novamente.')
        continue

    ## ENTRADA DOS NÚMEROS
    numero_1 = input('Digite um número: ').strip().replace(',', '.')
    numero_2 = input('Digite outro número: ').strip().replace(',', '.')

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
    except ValueError:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    ## CALCULO
    if operador == '+':
        resultado = num_1 + num_2
    elif operador == '-':
        resultado = num_1 - num_2
    elif operador == '*':
        resultado = num_1 * num_2
    elif operador == '/':
        if num_2 == 0:
            print('Erro: divisão por zero.')
            continue
        resultado = num_1 / num_2

    ## EXIBE O RESULTADO
    print(f'O RESULTADO DE {num_1} {operador} {num_2} = {resultado}\n')
