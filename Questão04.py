# Fase seguinte: Calculadora com loop usando dicionário de funções

# Por quê essa é a melhor agora?

# Você já entendeu como usar funções dentro de dicionários.

# Agora precisa aprender a controlar fluxo, repetir operações, validar entradas.

# É um passo natural antes de adicionar histórico.

# Então vamos pra versão com loop, mas mantendo o código limpo e profissional.

# 🎯 O que você deve fazer no exercício

# Criar uma calculadora que:

# ✔️ repete até o usuário digitar "sair"
# ✔️ usa o dicionário de funções -> OK
# ✔️ lê 2 números -> OK
# ✔️ lê uma operação (+ - * /) -> ok
# ✔️ executa e mostra o resultado -> ok
# ✔️ sem if gigante (apenas 1 if para validar operação) -> ok

def soma(a,b):
    return a+b
def dif(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

#Criando o dicionário de funções
operacoes = {
    "+": soma,
    "-": dif,
    "*": mult,
    "/": div
}
#Colocando dentro de um loop infinito
while True:

    #Saindo ou entrando no loop, reorganizando o fluxo do código.
    escolha = input("Digite uma operação, (+,-,*,/), caso queira 'sair' digite 'sair': ").lower() #Criando escolha

    if escolha in ("sair", "s"): #Essa é uma forma mais limpa de reescrever a condição
        print("Finalizando...")
        break
    if escolha not in operacoes:
        print("Operação inválida.")
        continue

    #Criando a leitura dos números
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    #Criando condição e tratamento de erro.
    if escolha == "/" and num2 == "0":
        print("Não é possível dividir por zero.")
    
    funcao = operacoes[escolha]
    resultado = funcao(num1, num2)

    print(f'{num1} {escolha} {num2} = {resultado}')
