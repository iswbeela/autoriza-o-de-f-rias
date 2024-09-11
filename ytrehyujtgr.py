def ferias(tempo,mes):
    if tempo >3:
        return "pedido de férias aprovado"
    elif mes not in [6,7,12,1]:
        return "férias fora da temporada"
    else:
        return "pedido de férias negado"
    
tempo = int(input("tempo de serviço: "))
mes = int(input("mes que deseja sair de férias: "))

resposta = ferias(tempo,mes)

print(resposta)