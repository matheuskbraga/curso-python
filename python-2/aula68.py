'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
'''
import os

def escopo(): # 'escopo' tem acesso apenas a x, pois x foi declarado globalmente
  def outra_funcao(): # esta função tem acesso a 'x' e 'y'
    y = 2
    print(x, y) # apenas a 'outra_funcao' tem acesso a y
  outra_funcao()
  print(x)

### OBS ###
# Se existir 2 variáveis de mesmo nome declaradas DENTRO e FORA da função a função irá priorizar a que está DENTRO.

os.system('cls')
x = 1
escopo()