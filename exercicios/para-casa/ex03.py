def dias_semana(num_dia):

    if num_dia == 1:
        return "Domingo"

    elif num_dia == 2:
        return "Segunda-feira"

    elif num_dia == 3:
        return "Terca-feira"

    elif num_dia == 4:
        return "Quarta-feira"

    elif num_dia == 5:
        return "Quinta-feira"

    elif num_dia == 6:  
        return "Sexta-feira"

    elif num_dia == 7:
        return "Sabado"

    else:
        return "inexistente"


numero_fornecido = int(input("Digite o número do dia de 1 à 7: "))


dia = dias_semana(numero_fornecido)

print(f"O dia da semana é {dia}!")