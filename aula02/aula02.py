from numba.core.cgutils import printf

print("ola mundo")

print(7 + 4)
print("7 + 4")
print("7" + "4") # concatenacao de strings

#comentario de 1 linha

''' 
comentario de 
multiplas 
linhas
'''

#VARIAVEIS
nome = "Victor" #str
idade = 19 #int
peso = 72.2 #float

print(nome, idade, peso)
print(f"Oi {nome}!!!")


# INPUT - SIMULACAO DE UM FORMS NO CMD
nome = input("Digite o seu nome")
idade = int(input ("Digite sua idade"))
peso = input ("Digite o seu peso")

nova_idade = idade = 1

print (nome, idade, peso)
print(nova_idade)