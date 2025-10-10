def verificar_feriado(mes, dia):
    match mes:
        case 1:
            match dia:
                case 1:
                    print(f"Feriado: Ano Novo")
                case _:
                    print(f"Não é feriado")
        case 2:
            print(f"esse mes nao tem feriado")
        case 3:
            print(f"esse mes nao tem feriado")
        case 3:
            print(f"esse mes nao tem feriado")
        case 4:
            match dia:
                case 21:
                    print(f"Feriado: Tiradentes")
                case _:
                    print(f"Não é feriado")
        case 5:
            match dia:
                case 1:
                    print(f"Feriado: Dia do Trabalhador")
                case _:
                    print(f"Não é feriado")
        case 6:
            print(f"esse mes nao tem feriado")
        case 7:
            print(f"esse mes nao tem feriado")
        case 8:
            print(f"esse mes nao tem feriado")
        case 9:
            match dia:
                case 7:
                    print(f"Feriado: Independencia do Brasil")
                case _:
                    print(f"Não é feriado")
        case 10:
            match dia:
                case 12:
                    print(f"Feriado: Dia das Crianças")
                case _:
                    print(f"Não é feriado")
        case 11:
            print(f"esse mes nao tem feriado")
        case 12:
            match dia:
                case 25:
                    print(f"Feriado: Natal")
                case _:
                    print(f"Não é feriado")


def main():
    mes = int(input("Digite o numero do mês (1-12): "))
    dia = int(input("Digite o dia do mês: "))
    verificar_feriado(mes, dia)



if __name__ == "__main__":
    main()



