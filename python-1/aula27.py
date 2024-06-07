"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print()
print(variavel[0:5:])  # 'i' e 'f' é o inicio e fim para cortar a string
print(len(variavel)) # len calcula o tamanho da string
print(variavel[0:9:2]) # o 'p' pula os espaços da string Ex: neste ex ele pula 2 e 2 caracteres
print(variavel[::-1]) # inverte a string
print(variavel[-1:-10:-1]) # inverte a string
print()