import pandas as pd
import glob

caminho_dos_csvs = 'dados/'
arquivos_csv = glob.glob(caminho_dos_csvs + "*.csv")
dataframes = [pd.read_csv(arquivo, encoding="latin1", delimiter=";") for arquivo in arquivos_csv]
df_combinado = pd.concat(dataframes, ignore_index=True)

pd.set_option('display.float_format', '{:.2f}'.format)

df_combinado['VALOR REALIZADO'] = df_combinado['VALOR REALIZADO'].str.replace(',','.')
df_combinado['VALOR REALIZADO'] = pd.to_numeric(df_combinado['VALOR REALIZADO'])

# Agrupando e somando [VALOR REALIZADO] por [ANO]
TotalporAno = df_combinado.groupby('ANO EXERCÍCIO')['VALOR REALIZADO'].sum().reset_index()

# Total por Categoria
TotalporCategoria = df_combinado.groupby('CATEGORIA ECONÔMICA')['VALOR REALIZADO'].sum().reset_index()

# Total de casos por estado
TotalporOrigem = df_combinado.groupby('ORIGEM RECEITA')['VALOR REALIZADO'].sum().reset_index()

# # Total de bitos por estado
# obitosNovosEstado = df_combinado.groupby('estado')['obitosNovos'].sum().reset_index()


with pd.ExcelWriter('dados/arquivo final/receitas.xlsx', engine='openpyxl') as writer:
     TotalporAno.to_excel(writer, sheet_name="Total por Ano", index=False)
     TotalporCategoria.to_excel(writer, sheet_name="Total por Categoria", index=False)
     TotalporOrigem.to_excel(writer, sheet_name="Total por Origem", index=False)
#     # obitosNovosEstado.to_excel(writer, sheet_name="Total de obitos por estado", index=False)

print('Arquivo gerado com sucesso')