import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Cria o app
app = dash.Dash(__name__)

# Define a função de formatação com suporte para milhões e valores menores
def format_value(valor):
    if valor >= 1e12:
        return "{:.1f}T".format(valor / 1e12)  # Trilhões
    elif valor >= 1e9:
        return "{:.1f}B".format(valor / 1e9)   # Bilhões
    elif valor >= 1e6:
        return "{:.1f}M".format(valor / 1e6)   # Milhões
    return "{:.0f}".format(valor)             # Valores menores

# Define os dados
df_porAno = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Ano")
df_porCategoria = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Categoria")
df_porOrigem = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Origem")
df_realizadoxprevisto = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Realizado x Previsto")
df_melted = df_realizadoxprevisto.melt(id_vars='ANO EXERCÍCIO', value_vars=['VALOR REALIZADO', 'VALOR PREVISTO ATUALIZADO'],
                           var_name='Tipo', value_name='Valor')

# Formatar os valores para os gráficos
df_porAno['VALOR REALIZADO FORMATADO'] = df_porAno['VALOR REALIZADO'].apply(format_value)
df_porCategoria['VALOR REALIZADO FORMATADO'] = df_porCategoria['VALOR REALIZADO'].apply(format_value)
df_porOrigem['VALOR REALIZADO FORMATADO'] = df_porOrigem['VALOR REALIZADO'].apply(format_value)
df_melted['Valor FORMATADO'] = df_melted['Valor'].apply(format_value)

# por Ano
grafico_porAno = px.line(df_porAno, x="ANO EXERCÍCIO", y="VALOR REALIZADO", text="VALOR REALIZADO FORMATADO", title="Total por ano")
grafico_porAno.update_traces(textposition='top center')

# por Categoria
grafico_porCategoria = px.bar(df_porCategoria, x="CATEGORIA ECONÔMICA", y="VALOR REALIZADO", text="VALOR REALIZADO FORMATADO", title="Total por Categoria Econômica")
grafico_porCategoria.update_traces(textposition='outside')

# por Origem
grafico_porOrigem = px.bar(df_porOrigem, x="ORIGEM RECEITA", y="VALOR REALIZADO", text="VALOR REALIZADO FORMATADO", title="Total por Origem da Receita")
grafico_porOrigem.update_traces(textposition='outside')

# por Previsto x Realizado
grafico_previsto_vs_realizado = px.line(df_melted, x="ANO EXERCÍCIO", y="Valor", color='Tipo', text="Valor FORMATADO", title="Total do Valor Previsto vs Realizado por Ano")
grafico_previsto_vs_realizado.update_traces(textposition='top center')

# Define o app
app.layout = html.Div(children=[
    html.H1(children="Relatório de Receitas do Governo Brasileiro (2014 - 2024)"),

    dcc.Graph(
        id="TotalporAno",
        figure=grafico_porAno
    ),

    dcc.Graph(
        id="TotalporCategoria",
        figure=grafico_porCategoria
    ),

    dcc.Graph(
        id="TotalporOrigem",
        figure=grafico_porOrigem
    ),    

    dcc.Graph(
        id="PrevistoVsRealizado",
        figure=grafico_previsto_vs_realizado
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
