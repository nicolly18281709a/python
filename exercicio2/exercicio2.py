precoCapa = 24.95
descontoLivraria = precoCapa * 0.40
precoCapaLivraria = precoCapa - descontoLivraria

fretePrimeiroExemplar = 3.00
freteRestanteExemplar = 0.75

custoAtacadoPrimeiroExemplar = precoCapaLivraria + fretePrimeiroExemplar
custoAtacado = custoAtacadoPrimeiroExemplar + ((precoCapaLivraria + freteRestanteExemplar)+50)

print("O custo total de atacado de 60 copias é de:")


