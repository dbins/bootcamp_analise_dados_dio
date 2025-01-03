# Solicita ao usuário uma lista de números separados por vírgula e os converte para ponto flutuante
numeros = list(map(float, input().split(',')))

# Define a função para calcular a mediana de uma lista de números
def calcular_mediana(numeros):
    # Ordena a lista de números em ordem crescente
    numeros_ordenados = sorted(numeros)
    # Obtém o comprimento da lista ordenada
    n = len(numeros_ordenados)
    # Calcula o ponto médio da lista
    ponto_medio = (n-1) // 2

    # TODO: Verifique se a quantidade de números é ímpar
    # Se for ímpar, retorna o valor no meio da lista
    # Se for par, retorna a média dos dois valores do meio da lista
    if (n % 2):
        return numeros_ordenados[ponto_medio]
    else:
        return (numeros_ordenados[ponto_medio] + numeros_ordenados[ponto_medio+1])/2.0

# Chama a função calcular_mediana com a lista de números como argumento e imprime o resultado
print(calcular_mediana(numeros))