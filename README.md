# 🌍 Dashboard Climático Global- ADS

## Visão Geral do Projeto

Este projeto demonstra a criação de um dashboard interativo para visualização de dados climáticos reais de diversas capitais globais. Desenvolvido com ferramentas gratuitas e de código aberto, o objetivo é fornecer um exemplo prático de um pipeline de dados completo, desde a coleta até a visualização, de forma acessível a qualquer pessoa, mesmo sem experiência prévia em programação.

## Funcionalidades

 **Coleta de Dados em Tempo Real:** Utiliza a API gratuita Open-Meteo para buscar dados climáticos atualizados.
**Visualização Interativa:** Apresenta temperaturas e velocidades do vento de forma clara e comparativa através de gráficos gerados com Plotly e exibidos no Streamlit.
 **Fácil de Usar:** Interface intuitiva e um botão para atualizar os dados com um clique.
**Código Aberto:** Todo o código é documentado e disponível para estudo e modificação.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Streamlit:** Framework para construção de dashboards web interativos.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **Requests:** Biblioteca para fazer requisições HTTP a APIs.
- **Plotly Express:** Biblioteca para criação de gráficos interativos.
- **Open-Meteo API:** Fonte de dados climáticos reais e gratuitos.


## Estrutura do Projeto

- `app.py`: O arquivo principal do Streamlit que constrói a interface do dashboard e exibe as visualizações.
- `data_fetcher.py`: Contém as funções responsáveis por se conectar à API Open-Meteo e coletar os dados climáticos.
- `requirements.txt`: Lista todas as bibliotecas Python necessárias para o projeto.
- `README.md`: Este arquivo, com a documentação do projeto.

## Entendendo o Código

### `data_fetcher.py`

Este script é o coração da coleta de dados. A função `get_weather_data` faz uma requisição HTTP para a API Open-Meteo, passando a latitude e longitude de uma cidade. Ela extrai a temperatura atual e a velocidade do vento. A função `get_all_cities_data` itera sobre uma lista pré-definida de cidades (São Paulo, Nova York, Londres, Tóquio, Paris) e coleta os dados para cada uma, retornando um DataFrame do Pandas.

### `app.py`

Este é o arquivo do Streamlit que cria o dashboard:

1.  **Configuração da Página:** Define o título da página e o layout.
2.  **Título e Introdução:** Exibe o título principal e uma breve descrição do projeto.
3.  **Botão de Atualização:** Permite ao usuário recarregar os dados mais recentes da API.
4.  **Coleta de Dados:** Chama a função `get_all_cities_data` do `data_fetcher.py`. Usa `@st.cache_data` para armazenar em cache os dados e evitar chamadas repetidas à API, melhorando a performance.
5.  **Métricas Principais:** Exibe cartões com a temperatura e vento atuais para cada cidade.
6.  **Gráficos Interativos:** Utiliza Plotly Express para criar:
    -   Um gráfico de barras comparando as temperaturas entre as cidades.
    -   Um gráfico de linha mostrando a velocidade do vento.
7.  **Tabela de Dados Brutos:** Mostra os dados coletados em formato de tabela.
8.  **Rodapé:** Informações adicionais sobre o projeto.

## Contribuições

Sinta-se à vontade para fazer um fork deste repositório, propor melhorias ou adicionar novas funcionalidades. Toda contribuição é bem-vinda!

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Para simplificar, não criaremos o arquivo LICENSE neste momento, mas é uma boa prática incluí-lo.)

## Contato

Para dúvidas ou sugestões, entre em contato através do GitHub.

