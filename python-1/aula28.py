print()
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
  idade_int = int(idade)
  print(f'Seu nome é {nome}')
  print(f'Você tem {idade} anos')
  print(f'Seu nome invertido é: {nome[::-1]}')
  print('Seu nome tem espaço: ',' ' in nome)
  print(f'Seu nome tem {(len(nome))} letras')
  print(f'A primeira letra do seu nome é: {nome[0]}')
  print(f'A última letra do seu nome é: {nome[-1]}')
else:
  print('Os espaços não foram preenchidos corretamente!')

print()