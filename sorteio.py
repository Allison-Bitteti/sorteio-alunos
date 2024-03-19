# Desenvolvido por: Allison Bitteti da Silva

def titulo(msg):
    msg = msg.strip().upper()

    print('~'*50)
    print(msg.center(50))
    print('~'*50)

def sorteio(lista):
    from random import choice
    from time import sleep

    cores = {
        'limpa': '\033[m',
        'vermelho': '\033[31m',
        'verde': '\033[32m'
    }

    tam = len(lista)
    for c in range(1, tam + 1):
        sleep(1)
        escolhido = choice(lista)

        if tam <= 10:
            metade = tam / 2
            if c <= metade:
                print(f'>>> {c}º: {cores["vermelho"]}{escolhido}{cores["limpa"]}')
            else:
                print(f'>>> {c}º: {cores["verde"]}{escolhido}{cores["limpa"]}')
        else:
            if c <= 5:
                print(f'>>> {c}º: {cores["vermelho"]}{escolhido}{cores["limpa"]}')
            elif c > (tam - 5):
                print(f'>>> {c}º: {cores["verde"]}{escolhido}{cores["limpa"]}')
            else:
                print(f'>>> {c}º: {escolhido}')
        lista.pop(lista.index(escolhido))

alunos = []

titulo('Sorteio de alunos')
qtd = int(input('Quantos alunos deseja sortear? '))

for a in range(1, qtd+1):
    aluno = input(f'{a}º Aluno(a): ').strip().capitalize()
    alunos.append(aluno)

titulo('Ordem Sorteada')
sorteio(alunos)
