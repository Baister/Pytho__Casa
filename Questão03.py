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

operacoes = { #Isso seria praticamente um dicionário de funções 
    "+": soma,
    "-": dif,
    "*": mult,
    "/": div
}

operacao = input("Qual operação quer fazer? (+,-,/,*) ?")

if operacao in operacoes: #Esse "in" é de caráter totalmente string, ou seja, se alguma string dentro da operacao estiver em operacoes, o programa consegue selecionar, sem precisar de loopings ou fórmulas.
    funcao = operacoes[operacao] #Aqui ele seleciona qual é a função
    resultado = funcao(num1, num2) #Aqui, coloca-se os valores dentro da função.
    print("Resultado: ",resultado)
else:
    print("Operação inválida!")

