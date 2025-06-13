def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(pi, raio):
    return (2 * raio) * pi

def calculaAreaCircunferencia(pi, raio):
    return pi * (raio ** 2)

# main
raio = int(input("digite o valor do raio"))
pi = 3,14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(raio,pi)
areaCircunferencia = calculaAreaCircunferencia

print("o valor do diametro é", diametro)
print("o valor da circunferencia é", circunferencia)
print("o valor da circunferencia é", areaCircunferencia)