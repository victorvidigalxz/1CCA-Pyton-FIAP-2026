# OPERADORESA DE ATRIBUICAO
from sqlalchemy.sql.operators import truediv

num = 15
print(num)

num = num + 2
print (num)

num *= 2
print (num)

# OPERADORES RELACIONAIS
print()
print(6 >= 6)

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade)

# OPERADOR LOGICO
# LOGICA E (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print (login)

if login:
    print("Entrar no programa")

print()

# NOTAS
nota_final = 7

if nota_final < 4:
    print("reprovado")
elif nota_final < 6:
    print("recuperacao")
else:
    print("Aprovado")

print("FIM")




