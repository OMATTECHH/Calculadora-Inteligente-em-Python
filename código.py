from calculadora import operacoes

def mostrar_menu():
    print('\n Escolha uma operação: ')
    print('1 - somar')
    print('2 - subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Potência')
    print('6 - Raiz quadrada')
    print('7 - fatorial')
    print('8 - Sair')

def obter_numero(mensagem):
    while True:
        try:
            return input(mensagem)
        except ValueError:
            print('Por favor, digite um número válido !')

print('Bem-vindo ao Calculadora!')

while True:
    mostrar_menu()
    escolha =  input('Digite sua escolha (1-8): ')

    if escolha == '8':
        print('Saindo...')
        break

    if escolha in ['1', '2', '3', '4', '5', '6']:
        numero1 = obter_numero('Digite o primeiro número: ')
        numero2 = obter_numero('Digite o segundo número: ')

        if escolha == '1':
            resultado = operacoes.soma(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif escolha == '2':
            resultado = operacoes.subtracao(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif escolha == '3':
            resultado = operacoes.multiplicacao(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif escolha == '4':
            resultado = operacoes.divisao(numero1, numero2)
            print(f'Resultado: {resultado}')
        elif escolha == '5':
            resultado = operacoes.potencia(numero1, numero2)
            print(f'Resultado: {resultado}')

    elif escolha == '6':
        numero1 = obter_numero('Digite um número: ')
        resultado = operacoes.raiz(numero1)
        print(f'Resultado: {resultado}')

    elif escolha == '7':
        numero1 = obter_numero('Digite um número inteiro não-negativo: ')
        try:
            numero1 = int(numero1)  # Converter para inteiro
            if numero1 >= 0:
                resultado = operacoes.fatorial(numero1)
                print(f'Resultado: {resultado}')
            else:
                print('Erro: Apenas números inteiros não-negativos são permitidos para fatoriais.')
        except ValueError:
            print('Erro: Você deve digitar um número inteiro válido.')