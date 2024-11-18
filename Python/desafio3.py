def crescimento_percentual(vendas_mensais):
    # TODO: Extraia os valores de venda de dois meses:
    valor_antigo = vendas_mensais[-2]['valor_venda']
    novo_valor = vendas_mensais[-1]['valor_venda']
    
    # TODO: Calcule o crescimento percentual
    crescimento = ((novo_valor - valor_antigo) / valor_antigo) * 100

    return crescimento
    

vendas_mensais = []

for i in range(2):
    mes = input()
    valor_venda = float(input())
    vendas_mensais.append({"mes": mes, "valor_venda": valor_venda})

# TODO: Chame a função e imprime o resultado:
resultado = crescimento_percentual(vendas_mensais)

print(f"Crescimento percentual de vendas: {resultado:.2f}%")