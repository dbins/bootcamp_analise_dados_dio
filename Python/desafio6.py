def calcular_producao():
    # Entrada de dados do usuário
    entrada = input()

    # Separando as entradas de cada região e produção
    regioes_producao = entrada.split(',')

    # TODO: Crie as variáveis para armazenar a produção total e o número de regiões
    total_producao = 0
    media_producao = 0
    
    # TODO: Itere sobre cada entrada de região: produção
    for registro in regioes_producao:
    
        # TODO: Divida a região e produção com base no caractere ":"
        regiao, producao = registro.split(': ')
        
        # TODO: Converta a produção para float e somando ao total
        total_producao += float(producao)

    # TODO: Calcule a média de produção por região
    media_producao = total_producao / len(regioes_producao)

    # Exibindo a produção total e média formatada
    print(f"Produção total: {total_producao:.2f} toneladas")
    print(f"Média por região: {media_producao:.2f} toneladas")

# Executa a função
calcular_producao()