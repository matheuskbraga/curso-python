"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''

print()
print('Exercício 1')
numero = input('Digite um número inteiro: ')

try:
  numero_inteiro = int(numero)
  if numero_inteiro % 2 == 0:
    print('O numero é par')
  else:
    print('O número é ímpar')
except:
  print('Este número não é inteiro')

print()
print('-------------------------------')

'''

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''
print()
print('Exercício 2')
hora = input('Quer horas são? ')
hora_int = int(hora)


if (hora_int >= 0) and (hora_int <= 11):
  print('Bom Dia!')
elif (hora_int >= 12) and (hora_int <= 17):
  print('Boa Tarde!')
elif (hora_int >= 18) and (hora_int <= 23):
  print('Boa Noite!')
else:
  print('Essa hora eu não conheço')
print()
print('-------------------------------')

'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print()
print('Exercício 3')
nome = input('Digite seu nome: ')
tamanho_nome = int(len(nome))

if tamanho_nome:
  if tamanho_nome <= 4:
    print('Seu nome é curto')
  elif tamanho_nome == 5 or tamanho_nome == 6:
    print('Seu nome é normal')
  else:
    print('Seu nome é muito grande')

print()
print('-------------------------------')