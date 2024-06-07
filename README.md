# Projeto de Rastreamento de Produtos do Mar

## Integrantes
-  Felipe Schineider - RM 552643
-  Thiago Araujo - RM 553477         
-  Vinicius Centurion - RM 554063

## Descrição do Projeto
Este projeto tem como objetivo criar um sistema de rastreabilidade de produtos do mar utilizando a linguagem Python. O sistema permite registrar, visualizar, salvar e carregar dados sobre produtos do mar, desde a captura até a venda. Além disso, utiliza a API OpenCage para obter as coordenadas geográficas dos locais de captura, processamento, transporte e venda.

## Funcionalidades
1. **Cadastrar Produto:**
   - Registro dos detalhes do produto, incluindo data e local de captura, processamento, transporte e venda.
   - Obtenção de coordenadas geográficas dos locais informados, ou através de coleta automática.

2. **Visualizar Produtos:**
   - Listagem de todos os produtos cadastrados com detalhes completos.

3. **Salvar Dados:**
   - Salvamento dos dados dos produtos em um arquivo JSON.

4. **Carregar Dados:**
   - Carregamento dos dados dos produtos a partir de um arquivo JSON.

5. **Deletar Produto:**
   - Remoção de um produto específico pelo nome.

## Instruções de Uso
1. **Clone o repositório:**
   ```bash
   git clone [URL do repositório]
   cd [nome do repositório]
## Requisitos

- Python 3.x
- Biblioteca `requests`

## Dependências

- `requests`: Para realizar requisições HTTP à API do OpenCage.
- - `datetime`: Para realizar a coleta automática das coordenadas.

## Estrutura do Projeto

- `main.py`: Arquivo principal contendo o código do sistema.
- `produtos.json`: Arquivo JSON onde os dados dos produtos são salvos (criado automaticamente ao salvar dados).

## Instalação

1. **Instale as dependências:**

    Este projeto utiliza a biblioteca `requests`. Você pode instalá-la usando pip:

    ```bash
    pip install requests
    ```

2. **Obtenha uma chave de API do OpenCage:**

    - Crie uma conta gratuita no [OpenCage Geocoder](https://opencagedata.com/).
    - Obtenha sua chave da API e substitua `'SUA_CHAVE_API'` no código pela sua chave.

3. **Execute o script principal:**

    ```bash
    python main.py
    ```

## Uso

- **Navegue pelo menu:**
  
  Utilize as opções do menu para cadastrar produtos, visualizar produtos, salvar dados, carregar dados ou deletar produtos.

## Tratamento de Exceções

O sistema inclui tratamento de exceções para garantir robustez ao lidar com erros inesperados, como falhas na leitura/escrita de arquivos e na obtenção de coordenadas geográficas.

## Considerações Finais

Este projeto foi desenvolvido com o objetivo de aplicar conhecimentos básicos de Python em um contexto prático. A integração com a API do OpenCage adiciona uma camada adicional de funcionalidade, permitindo o aprendizado sobre requisições HTTP e processamento de dados externos.
