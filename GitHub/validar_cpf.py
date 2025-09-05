import re
import sys
import os

# cpf = '746.824.890-70'
entrada = input('Por favor Insira seu CPF para validação: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
    )

if not cpf or len(cpf) != 11:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('❌ CPF inválido: o CPF deve conter exatamente 11 dígitos.')
    sys.exit()

if cpf == cpf[0] * len(cpf):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('❌ CPF inválido: sequência de dígitos não é permitida.')
    sys.exit()

try:
    nove_digitos = cpf[:9]
    multiplicador = 10
    soma = 0

    for numero in nove_digitos:
        soma += int(numero) * multiplicador
        multiplicador -= 1

    resto = (soma * 10) % 11
    digito1 = 0 if resto > 9 else resto

    dez_digitos = nove_digitos + str(digito1)
    multiplicador = 11
    soma = 0

    for numero in dez_digitos:
        soma += int(numero) * multiplicador
        multiplicador -= 1

    resto = (soma * 10) % 11
    digito2 = 0 if resto > 9 else resto

    cpf_calculado = f"{nove_digitos}{digito1}{digito2}"

    if cpf == cpf_calculado:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'✅ CPF {cpf} é válido!')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'❌ CPF {cpf} é inválido!')

except Exception as e:
    print("Erro no cálculo:", e)
