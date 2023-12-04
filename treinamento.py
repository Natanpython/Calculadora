s = 0
for n in range(0, 5):
    n = int(input('Digite um numero: '))
    s += n
print(f'A soma foi {s}')

----------------------------------------------------------------------------------------------------------
for c in range(0, 50+1):
    if c % 2 == 0:
        print(c, end=' ')

--------------------------------------------------------------------------------------------------------------
soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'valores selecionados é {cont} A soma de todos os valores é  {soma}')

--------------------------------------------------------------------------------------------------------------------
num = int(input('Digite um numero: '))
tot = 0
for c in range(2, num+1):
    if num % c == 0:
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\033[mO numero {num} foi divizivel {tot} vezes')
if tot == 2:
    print('é por isso que ele é Primo!')
else:
    print(' Ele nao é primo!')

-----------------------------------------------------------------------------------------------
from random import randint
computador = randint(0,10)
print('Sou seu Computador... Pensei em um numero de 0 10!')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print(f'Acertou com {palpites} tentativas, PARABENS')

-----------------------------------------------------------------------------------------------
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''Escolha uma Opição
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] MENOR
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opçao = int(input('Digite uma Opição: '))
    if opçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} = {soma}')
    elif opçao == 2:
        soma = n1 * n2
        print(f'A Mulriplicação entre {n1} e {n2} = {soma}')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O numero maior entre {n1} e {n2} = {maior}')
    elif opçao == 4:
        if n1 < n2:
            menor = n1
        else:
            menor = n2
        print(f'O numero menor entre {n1} e {n2} = {menor}')
    elif opçao == 5:
        print('FINALIZADO...')
    else:
        print('Opição invalida, Tente Novamente: ')
print('FIM de programa< Volte Sempre!')

----------------------------------------------------------------------------------
num = int(input('Digite numero para ver fatorial: '))
c = num
f = 1
print(f'Calculando o fatorial de {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ',end='')
    f *= num
    c -= 1
print(f'{f}')

--------------------------------------------------------------------------------------------------

print('=' * 30)
print('         Gerador de PA')
print('=' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->',end=' ')
    cont += 1
    termo += razao
print(' FIM')

----------------------------------------------------------------------------------------------------------------

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->',end=' ')
        cont += 1
        termo += razao
    print(' Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('FIM')

