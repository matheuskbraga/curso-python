'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
'''
import os
import decimal

os.system('cls')
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)           # 0.799999999999999999
print(f'{numero_3:.2f}')  # 0.80

print(round(numero_3, 2)) # 'round' recebe o número e coloca o número de casas decimais

print('--------------------------------------')

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)           
print(f'{numero_3:.2f}')  
print(round(numero_3, 2))