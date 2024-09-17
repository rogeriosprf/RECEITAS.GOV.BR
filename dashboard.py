import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Cria o app
app = dash.Dash(__name__)

# Define os dados
df_porAno = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Ano")
df_porCategoria = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Categoria")
df_porOrigem = pd.read_excel("dados/arquivo final/receitas.xlsx", sheet_name="Total por Origem")

grafico_porAno  = px.line(df_porAno, x="ANO EXERCÍCIO", y="VALOR REALIZADO", text="VALOR REALIZADO", title="Total por ano")
grafico_porAno.update_traces(textposition='top center')

grafico_porCategoria = px.bar(df_porCategoria, x="CATEGORIA ECONÔMICA", y="VALOR REALIZADO", title="Total por Categoria Econômica")
grafico_porOrigem = px.bar(df_porOrigem, x="ORIGEM RECEITA", y="VALOR REALIZADO", title="Total por Origem da Receita")

# Define o app
app.layout = html.Div(children=[
    html.H1(children="Relatório de Receitas"),

    dcc.Graph(
        id="TotalporAno",
        figure=grafico_porAno
    ),

    dcc.Graph(
        id="TotalporCategoria",
        figure=grafico_porCategoria
    ),

    dcc.Graph(
        id="TotalporCategoria",
        figure=grafico_porOrigem
    ),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
