import requests
import json
import os

# Estrutura básica de dados para armazenar os produtos
produtos = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    produto = {}
    produto['nome'] = input("Nome do Produto: ")
    produto['captura'] = {
        'data': input("Data da Captura: "),
        'local': input("Local da Captura: ")
    }
    produto['processamento'] = {
        'data': input("Data do Processamento: "),
        'local': input("Local do Processamento: ")
    }
    produto['transporte'] = {
        'data': input("Data do Transporte: "),
        'local': input("Local do Transporte: ")
    }
    produto['venda'] = {
        'data': input("Data da Venda: "),
        'local': input("Local da Venda: ")
    }

    # Obter coordenadas usando OpenStreetMap Nominatim API
    endereco = produto['captura']['local']  # Use o local da captura como exemplo
    coordenadas = obter_coordenadas(endereco)
    if coordenadas:
        produto['coordenadas'] = coordenadas

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def obter_coordenadas(endereco):
    try:
        url = f'https://nominatim.openstreetmap.org/search?q={endereco}&format=json'
        response = requests.get(url)
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return {'latitude': latitude, 'longitude': longitude}
        else:
            print("Endereço não encontrado.")
            return None
    except Exception as e:
        print("Erro ao conectar à API:", e)
        return None

# Função para visualizar todos os produtos
def visualizar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for i, produto in enumerate(produtos, start=1):
        print(f"\nProduto {i}:")
        print(f"Nome: {produto['nome']}")
        print(f"Captura - Data: {produto['captura']['data']}, Local: {produto['captura']['local']}")
        print(f"Processamento - Data: {produto['processamento']['data']}, Local: {produto['processamento']['local']}")
        print(f"Transporte - Data: {produto['transporte']['data']}, Local: {produto['transporte']['local']}")
        print(f"Venda - Data: {produto['venda']['data']}, Local: {produto['venda']['local']}")
        if 'coordenadas' in produto:
            print(f"Coordenadas: Latitude {produto['coordenadas']['latitude']}, Longitude {produto['coordenadas']['longitude']}")

# Função para salvar os dados em um arquivo JSON
def salvar_dados():
    try:
        with open('produtos.json', 'w') as f:
            json.dump(produtos, f)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# Função para carregar os dados de um arquivo JSON
def carregar_dados():
    global produtos
    try:
        if os.path.exists('produtos.json'):
            with open('produtos.json', 'r') as f:
                produtos = json.load(f)
            print("Dados carregados com sucesso!")
        else:
            print("Arquivo de dados não encontrado. Um novo arquivo será criado ao salvar.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

# Função para deletar um produto
def deletar_produto():
    visualizar_produtos()
    if produtos:
        indice = int(input("Digite o índice do produto a ser deletado: ")) - 1
        if 0 <= indice < len(produtos):
            del produtos[indice]
            print("Produto deletado com sucesso!")
        else:
            print("Índice inválido.")
    else:
        print("Nenhum produto cadastrado.")

# Função principal para exibir o menu e processar as escolhas do usuário
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Visualizar Produtos")
        print("3. Deletar Produto")
        print("4. Salvar Dados")
        print("5. Carregar Dados")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            visualizar_produtos()
        elif escolha == '3':
            deletar_produto()
        elif escolha == '4':
            salvar_dados()
        elif escolha == '5':
            carregar_dados()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    carregar_dados()
    menu()
