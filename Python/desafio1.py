def filtrar_funcionarios(funcionarios, cargo):
    # TODO: Filtre os funcionários pelo cargo especificado
    return [func['nome'] for func in funcionarios if func['cargo'] == cargo]

# Função para entrada do usuário
def main_filtro():
    n = int(input())
    funcionarios = []

    for _ in range(n):
        id_funcionario = int(input())
        nome = input()
        cargo = input()
        funcionarios.append({"id": id_funcionario, "nome": nome, "cargo": cargo})

    cargo_filtro = input()
    resultado = filtrar_funcionarios(funcionarios, cargo_filtro)
    
    print(resultado)

# Executando a função
main_filtro()