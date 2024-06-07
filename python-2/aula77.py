# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

os.system('cls') # limpa o terminal
#print(len(perguntas)) # 3 valores (dicionarios) dentro da lista, uma em cada posição
qtd_acertos = 0 # quantidade de acertos igual a zero
for pergunta in perguntas: # navega nas posições da lista
    print('Pergunta:', pergunta['Pergunta']) # na posição da lista ela procura a chave 'Pergunta' e printa
    print()

    opcoes = pergunta['Opções'] # pega os valores (lista) apontados pela chave 'Opções' e salva na variável 'opcoes'

    for i, opcao in enumerate(opcoes): # pega todos os valores da lista e enumera eles, utilizando a função enumerate e a variável 'i' para colocar seus numeros
        print(f'{i})', opcao) # printa as opções com seus respectivos números
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit(): # verifica se os digitos são numeros de 0 a 9, caso contrário a função retorna um False
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou ✅')
    else:
        print('Errou ❌')

    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')