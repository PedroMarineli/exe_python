import os

def exibir_opcoes():
    print('Exercícios em Python\n')
    print('1. Par ou ímpar')
    print('2. Idade')
    print('3. Usuário e senha')
    print('4. Coordenadas')
    print('5. Crie e percorra uma lista')
    print('6. Soma dos números ímpares de 1 a 10')
    print('7. Números de 1 a 10 em ordem decrescente')
    print('8. Tabuada')
    print('9. Soma de todos os elementos')
    print('10. Média dos valores')

    print()



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                par_ou_impar()
            case 2:
                print('2')
            case 3:
                print('3')
            case 4:
                print('4')
            case 5:
                print('5')
            case 6:
                print('6')
            case 7:
                print('7')
            case 8:
                print('8')
            case 9:
                print('9')
            case 10:
                print('10')
            case _:
                print('opção inválida')
    except:
        print('opção inválida')

def main():
    os.system('clear')
    exibir_opcoes()
    escolher_opcao()

def par_ou_impar():
    exibir_titulo('Par ou ímpar')
    if int(input('\nDigite um número: ')) % 2 == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é ímpar')

def exibir_titulo(texto):
    os.system('clear')
    print(texto)
    print()

if __name__ == '__main__':
    main()