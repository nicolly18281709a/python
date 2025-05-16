print("valor do primeiro trecho: 8 min e 15 s")
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15
totalTempoPrimeiroTrecho = minutoPrimeiroTrecho + segundoPrimeiroTrecho
print("tempo do primeiro trecho em segundos:", totalTempoPrimeiroTrecho)

print("tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundoSegundoTrecho = 12
totalTempoSegundoTrecho = minutoSegundoTrecho + segundoSegundoTrecho
print("tempo do segundo trecho em segundos:", totalTempoSegundoTrecho)

print("tempo do terceiro trecho: 8 min e 15 s")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15
totalTempoTerceiroTrecho = minutoTerceiroTrecho + segundoTerceiroTrecho
print("tempo do terceiro trecho em segundos:", totalTempoTerceiroTrecho)

# Soma o total de minutos e converte para segundos
totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

# Soma valor total dos segundos
totalTempoTodosTrechosSegundos = (segundoPrimeiroTrecho + segundoSegundoTrecho + segundoTerceiroTrecho)

restanteMinuto = int(totalTempoTodosTrechosMinutos / 60)
restanteSegundo = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechos + restanteMinuto
totalSegundos = totalTempoTodosTrechos + restanteSegundo


print("soma de tempo de todos os trechos:", totalMinutos, "minutos")
print("soma de tempo de todos os trechos:", totalSegundos, "segundos")

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
print(horaInicialSegundos)
print(minutoInicialSegundos)
horarioInicialSegundos = horaInicialSegundos + horaInicialSegundos


tempoTrechoMinutosSegundos = totalMinuto * 60


horaChegada = int((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60 / 60)
minutosChegadas = int((minutoInicialSegundos + tempoTrechoMinutosSegundos) / 60 % 60)

