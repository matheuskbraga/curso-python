import os

os.system('cls')
cpf = '74682489070'
nove_digitos = cpf[:9]
#print(nove_digitos)
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
  resultado_digito_1 += int(digito) * contador_regressivo_1
  contador_regressivo_1 -= 1
#print(resultado_digito_1)

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_1 in dez_digitos:
  resultado_digito_2 += int(digito) * contador_regressivo_2
  contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
#print(digito_2)

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
  print(f'{novo_cpf} é válido!')