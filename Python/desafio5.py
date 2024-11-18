def analisar_desempenho_funcionarios():
    # Entrada de dados
    registros = input()
    desempenho = []

    # Processamento dos dados
    for registro in registros.split(', '):
        nome, pontuacao = registro.split(': ')
        pontuacao = int(pontuacao)
        resultado = ""


        # TODO: Implemente a solução para a classificação de desempenho:
        if pontuacao < 75:
            resultado = "Regular"
        elif pontuacao < 91:
            resultado = "Bom"
        else:
            resultado = "Excelente"

        desempenho.append(f"{nome}: {resultado}")
        


    # TODO: Agora, exiba a saída:
    for item in desempenho:
        print(item)
    

analisar_desempenho_funcionarios()