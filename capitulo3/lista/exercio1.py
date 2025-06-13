#funcao input receber e guarda o dado
# int tem como funcao converte


def soma(numero1, numero2):
    print("o resultado da adicao é:", numero1 + numero2)

def subtracao(numero1, numero2):
    print("o resultado da subtracao é:", numero1 - numero2)

def multiplicacao(numero1, numero2):
    print("o resultado da multiplicacao é:", numero1 * numero2)

def divisao(numero1, numero2):
    resultado_divisao = numero1 / numero2
    print("o resultado da divisao é:", resultado_divisao)

numero1 = int(input("digitar o 1 numero"))
numero2 = int(input("digitar o 2 numero"))

soma(numero1, numero2)
subtracao(numero1, numero2)
multiplicacao(numero1, numero2)
divisao(numero1, numero2)
