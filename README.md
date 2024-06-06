Aluno
Nome: [Seu Nome]
RM: [Seu RM]
Descrição do Projeto
Este projeto tem como objetivo criar um sistema de rastreabilidade de produtos do mar utilizando a linguagem Python. O sistema permite registrar, visualizar, salvar e carregar dados sobre produtos do mar, desde a captura até a venda. Além disso, utiliza a API OpenCage para obter as coordenadas geográficas dos locais de captura, processamento, transporte e venda.

Funcionalidades
Cadastrar Produto:

Registro dos detalhes do produto, incluindo data e local de captura, processamento, transporte e venda.
Obtenção de coordenadas geográficas dos locais informados.
Visualizar Produtos:

Listagem de todos os produtos cadastrados com detalhes completos.
Salvar Dados:

Salvamento dos dados dos produtos em um arquivo JSON.
Carregar Dados:

Carregamento dos dados dos produtos a partir de um arquivo JSON.
Deletar Produto:

Remoção de um produto específico pelo nome.
Instruções de Uso
Clone o repositório:

bash
Copiar código
git clone [URL do repositório]
cd [nome do repositório]
Instale as dependências:

Este projeto utiliza a biblioteca requests. Você pode instalá-la usando pip:
bash
Copiar código
pip install requests
Obtenha uma chave de API do OpenCage:

Crie uma conta gratuita no OpenCage Geocoder.
Obtenha sua chave da API e substitua 'SUA_CHAVE_API' no código pela sua chave.
Execute o script principal:

bash
Copiar código
python main.py
Navegue pelo menu:

Utilize as opções do menu para cadastrar produtos, visualizar produtos, salvar dados, carregar dados ou deletar produtos.
Requisitos
Python 3.x
Biblioteca requests
Dependências
requests: Para realizar requisições HTTP à API do OpenCage.
Estrutura do Projeto
main.py: Arquivo principal contendo o código do sistema.
produtos.json: Arquivo JSON onde os dados dos produtos são salvos (criado automaticamente ao salvar dados).
Tratamento de Exceções
O sistema inclui tratamento de exceções para garantir robustez ao lidar com erros inesperados, como falhas na leitura/escrita de arquivos e na obtenção de coordenadas geográficas.
Considerações Finais
Este projeto foi desenvolvido com o objetivo de aplicar conhecimentos básicos de Python em um contexto prático, abrangendo manipulação de listas, strings, funções, estruturas de dados, manipulação de arquivos e tratamento de exceções. A integração com uma API externa (OpenCage) adiciona uma camada adicional de funcionalidade e aprendizado sobre requisições HTTP e processamento de dados externos.
