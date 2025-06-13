# uma funcao pode chamar outra funcao

def mostrar_nome_inteiro(nome, sobrenome):
    print(nome)
    sobrenome(sobrenome)

def sobrenome(sobrenome):
    print(sobrenome)

    nome = "jose"
    sobrenome = "valin"
    mostrar_nome_inteiro(nome, sobrenome)

# cat_twice faz a concatenacao entre um e dois (part1 + part2)
# print_twice imprime as coisas duas vezes