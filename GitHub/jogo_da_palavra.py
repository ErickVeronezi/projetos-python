import os

palavra_secreta = ('ESTUDANTE')
letras_acertadas = ''
numero_de_tentivas = 0

while True:
    numero_de_tentivas += 1
    letras_digitadas = input('Digite uma letra: ').strip().upper()

    if len(letras_digitadas) > 1:
        print('Digite APENAS uma letra.')
        continue

    if letras_digitadas not in palavra_secreta:
        print(f'A letra {letras_digitadas} Não está na palavra.')
        continue

    if letras_digitadas in palavra_secreta:
        letras_acertadas += letras_digitadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            f'Parabéns!! Você acertou a palavra!!\n'
            f'A palavra era: {palavra_secreta}\n'
            f'Seu número de tentativas foi: {numero_de_tentivas}'
        )
        letras_acertadas = ''
        numero_de_tentivas = 0
        break

