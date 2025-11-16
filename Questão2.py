#Fazendo exercícios para melhorar a lógica
#Transformando funções em uma só

# Exercício 1 — Transformar funções repetidas em uma só

# Crie uma função que recebe:

# dois números

# um operador (+, -, *, /)

# E retorna o resultado.

# Sem if dentro do menu.

# def soma(a, b):
#     return a+b

# resultado = soma(10,20)
# print(resultado)

# def diferenca(a,b):
#     return a-b

# resultado = diferenca(10,20)
# print(resultado)

# def multiplica(a,b):
#     return a * b
# resultado = multiplica(10,20)
# print(resultado)

# def div(a,b):
#     return a/b

# resultado = div(10,20)
# print(resultado)

#Para a questão, eu compreendi o conceito de uma função pura.

#Agora reorganizando ela para uma maneira mais legível

def soma(a,b):
    return a+b

def dif(a,b):
    return a-b

def multip(a,b):
    return a*b

def div(a,b):
    return a/b

print(soma(10,20))
print(dif(10,20))
print(multip(10,20))
print(div(10,20))