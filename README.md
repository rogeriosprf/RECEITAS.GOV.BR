# Relatório de Receitas e Despesas
Este é um aplicativo desenvolvido em Dash para visualização de dados de receitas. Ele oferece gráficos interativos que apresentam as receitas totais por ano, categoria econômica e origem, além de comparar os valores previstos e realizados.

Funcionalidades
Gráficos interativos para visualização de receitas:
Total por Ano
Total por Categoria Econômica
Total por Origem da Receita
Comparação entre Valores Previsto e Realizado por Ano
Tecnologias Utilizadas
Python
Dash
Plotly
Pandas
Estrutura do Código
Importação de bibliotecas: As bibliotecas necessárias são importadas, incluindo Dash, Plotly e Pandas.
Criação do aplicativo: Um objeto Dash é criado para iniciar o aplicativo.
Função de formatação: Uma função personalizada format_value é definida para formatar valores em trilhões, bilhões e milhões.
Leitura dos dados: Os dados são lidos a partir de um arquivo Excel contendo várias planilhas.
Preparação dos dados: Os dados são processados e formatados para uso nos gráficos.
Criação dos gráficos: Gráficos são gerados usando Plotly Express.
Definição do layout do aplicativo: O layout do aplicativo é definido com títulos e gráficos.
Como Executar
Clone o repositório:

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>
Instale as dependências: Certifique-se de ter Python instalado e, em seguida, instale as bibliotecas necessárias:

bash
Copiar código
pip install dash plotly pandas openpyxl
Execute o aplicativo:

bash
Copiar código
python <NOME_DO_ARQUIVO>.py
Acesse o aplicativo: Abra um navegador e acesse http://127.0.0.1:8050/.

Observações
Certifique-se de que o arquivo Excel receitas.xlsx esteja na pasta dados/arquivo final/ com as planilhas apropriadas.
O aplicativo é executado em modo de depuração, facilitando o desenvolvimento e a resolução de problemas.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
