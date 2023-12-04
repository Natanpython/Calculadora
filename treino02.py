from time import sleep
print('=' * 30)
print('          Calculadora')
print('=' * 30)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opiçao = 0
while opiçao != 6:
    print('''    [ 1 ] SOMA
    [ 2 ] SUBITRAÇÂO
    [ 3 ] MULTIPLICAÇÂO
    [ 4 ] DIVISÂO
    [ 5 ] Novos NUMEROS
    [ 6 ] SAIR DO PROGRAMA''')
    opiçao = int(input('Qual calculo deseja: '))
    print('=' * 30)
    print('CALCULANDO...')
    sleep(1)

    if opiçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')

    elif opiçao == 2:
        sub = n1 - n2
        print(f'A Subitração entre {n1} - {n2} = {sub}')

    elif opiçao == 3:
        mult = n1 * n2
        print(f'A Multiplicação entre {n1} X {n2} ={mult}')

    elif opiçao == 4:
        div = n1 / n2
        print(f'A Divisão entre {n1} / {n2} = {div}')

    elif opiçao == 5:
        n1 = int(input('Digite novo numero: '))
        n2 = int(input('Mais um numero: '))

    elif opiçao == 6:
        print('Finalizando o programa...')
        sleep(1)
        print("CARREGANDO...")
        sleep(0.5)

    else:
        print('Opção invalida! Por Favor informar opção correta: ')

print('=' * 30)
print('Volte Sempre!....')
print('=' * 30)
