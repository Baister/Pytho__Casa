# Exercício 2 — Agora sim com input e validação

# Cria um programa que:

# Pergunta dois números ao usuário (use input()).

# Usa as funções que você criou (soma, diferença, etc.).

# Pede ao usuário qual operação ele quer fazer (+, -, *, /).

# Faz a operação escolhida sem usar if gigante nem match.
# Use um dicionário de funções (isso é o novo aprendizado).

#Se o usuário digitar um operador inválido, o programa avisa.


def soma(a,b):
    return a+b
def dif(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))


