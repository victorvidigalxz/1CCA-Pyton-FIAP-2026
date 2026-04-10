def print_lyrics():
    print("I ain't gonna live forever")
    print("I just wanna to live while I'm alive")

print_lyrics()
print_lyrics()

print()  # pular linha

def boas_vindas(nome):
    print(f"Ola, {nome}!!! seja bem vindo!!!!!")

boas_vindas("Alexendre")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(34, 78)
print(soma(34, 78))
print(type(nome_digitado))