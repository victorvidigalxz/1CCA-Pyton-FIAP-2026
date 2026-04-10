# imagina um prpograma... que recebe a escolha do usuario
# escolha_usuario
# 0 --> sar d programa
# 1 --> entrar no programa
# ----> erro!

escolha_usuario = 1

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("erro")
