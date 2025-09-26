def validaIdade(idade):
    if(idade >= 18):
        print("voce é maior de idade")
    else:
        print("voce é menor de idade")

idade = int(input("Digite sua idade"))

validaIdade(idade)