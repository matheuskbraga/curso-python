nome = 'Matheus Braga'
altura = 1.85
peso = 85
imc = ...

calculo_imc = peso / altura ** 2

# f-strings
# variaveis dentro de texto
# colocar um 'f' no inicio do texto
# colocar :.2f para controlar casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura'

linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{calculo_imc:.2f}'

print()
print(linha_1)
print(linha_2)
print(linha_3)
print()