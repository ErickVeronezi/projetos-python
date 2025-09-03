lista_compras = []
import os

while True:
    menu = input('\t[I]nsert [D]elete [L]istar:\n\t========  [S]air  ========\n> ').strip().upper()

    if menu not in {'I', 'D', 'L', 'S'}:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\tOpção inválida.\n\tDigite apenas a primeira letra da opção escolhida (I/D/L/S).')
        continue

    elif menu == 'D':
        os.system('cls' if os.name == 'nt' else 'clear')

        if not lista_compras:
            print('A lista está vazia. Nada para deletar.')
            continue

        deletados = input('Escolha o índice de um item para deletar: ').strip()
        try:
            deletar = int(deletados)
            removido = lista_compras[deletar]  # para confirmar o item
            del lista_compras[deletar]
            print(f'Item removido: {removido}')
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print(f'Índice {deletados} não existe.')
        except Exception as e:
            print(f'Erro: {e}')
        continue

    elif menu == 'I':
        os.system('cls' if os.name == 'nt' else 'clear')
        insert = input('Qual nome do produto você deseja inserir? ').strip()
        if insert:
            lista_compras.append(insert)
            print(f'Item adicionado: {insert}')
        else:
            print('Nada inserido (campo vazio).')
        continue

    elif menu == 'L':
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(lista_compras) == 0:
            print('Nada na lista.')
        else:
            print('Itens na lista:')
            for indice, nome in enumerate(lista_compras, start=0):
                print(indice, nome)
        continue

    if menu == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você está saindo...')
        break
