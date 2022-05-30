import streamlit as sl
import matplotlib.pyplot as plt
import numpy as np
import tabula
import pandas as pd
import plotly as pl
import plotly.graph_objects as go
import plotly.express as px
from tabula.io import read_pdf


plt.rcParams['figure.figsize'] = (11,7)

pdf_path_12019 = "./Trimestrais/1_2019.pdf"
pdf_path_22019 = "./Trimestrais/2_2019.pdf"
pdf_path_32019 = "./Trimestrais/3_2019.pdf"
pdf_path_42019 = "./Trimestrais/4_2019.pdf"
pdf_path_12020 = "./Trimestrais/1_2020.pdf"
pdf_path_22020 = "./Trimestrais/2_2020.pdf"
pdf_path_32020 = "./Trimestrais/3_2020.pdf"
pdf_path_42020 = "./Trimestrais/4_2020.pdf"
pdf_path_12021 = "./Trimestrais/1_2021.pdf"
pdf_path_22021 = "./Trimestrais/2_2021.pdf"
pdf_path_32021 = "./Trimestrais/3_2021.pdf"
pdf_path_42021 = "./Trimestrais/4_2021.pdf"
pdf_path_12022 = "./Trimestrais/1_2022.pdf"

tabelas12019 = tabula.io.read_pdf(pdf_path_12019, pages='1-2')
tabelas22019 = tabula.io.read_pdf(pdf_path_22019, pages='1-2')
tabelas32019 = tabula.io.read_pdf(pdf_path_32019, pages='1-2')
tabelas42019 = tabula.io.read_pdf(pdf_path_42019, pages='1-2')
tabelas12020 = tabula.io.read_pdf(pdf_path_12020, pages='1-2')
tabelas22020 = tabula.io.read_pdf(pdf_path_22020, pages='1-2')
tabelas32020 = tabula.io.read_pdf(pdf_path_32020, pages='1-2')
tabelas42020 = tabula.io.read_pdf(pdf_path_42020, pages='1-2')
tabelas12021 = tabula.io.read_pdf(pdf_path_12021, pages='1-2')
tabelas22021 = tabula.io.read_pdf(pdf_path_22021, pages='1-2')
tabelas32021 = tabula.io.read_pdf(pdf_path_32021, pages='1-2')
tabelas42021 = tabula.io.read_pdf(pdf_path_42021, pages='1-2')
tabelas12022 = tabula.io.read_pdf(pdf_path_12022, pages='1-2')

df1_12020 = tabelas12020[0]
df2_12020 = tabelas12020[1]
df3_12020 = tabelas12020[2]
df1_12020.insert(0, "Sem_Ano", ["1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020",])
df2_12020.insert(0, "Sem_Ano", ["1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020"])

df1_22020 = tabelas22020[0]
df2_22020 = tabelas22020[1]
df3_22020 = tabelas22020[2]
df1_22020.insert(0, "Sem_Ano", ["2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020",])
df2_22020.insert(0, "Sem_Ano", ["2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020"])

df1_32020 = tabelas32020[0]
df2_32020 = tabelas32020[1]
df3_32020 = tabelas32020[2]
df1_32020.insert(0, "Sem_Ano", ["3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020",])
df2_32020.insert(0, "Sem_Ano", ["3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020"])

df1_42020 = tabelas42020[0]
df2_42020 = tabelas42020[1]
df3_42020 = tabelas42020[2]
df1_42020.insert(0, "Sem_Ano", ["4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020",])
df2_42020.insert(0, "Sem_Ano", ["4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020"])

df1_12021 = tabelas12021[0]
df2_12021 = tabelas12021[1]
df3_12021 = tabelas12021[2]
df1_12021.insert(0, "Sem_Ano", ["1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021",])
df2_12021.insert(0, "Sem_Ano", ["1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021"])

df1_22021 = tabelas22021[0]
df2_22021 = tabelas22021[1]
df3_22021 = tabelas22021[2]
df1_22021.insert(0, "Sem_Ano", ["2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021",])
df2_22021.insert(0, "Sem_Ano", ["2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021"])

df1_32021 = tabelas32021[0]
df2_32021 = tabelas32021[1]
df3_32021 = tabelas32021[2]
df1_32021.insert(0, "Sem_Ano", ["3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021",])
df2_32021.insert(0, "Sem_Ano", ["3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021","3_2021"])

df1_42021 = tabelas42021[0]
df2_42021 = tabelas42021[1]
df3_42021 = tabelas42021[2]
df1_42021.insert(0, "Sem_Ano", ["4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021",])
df2_42021.insert(0, "Sem_Ano", ["4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021","4_2021"])

df1_12022 = tabelas12022[0]
df2_12022 = tabelas12022[1]
df3_12022 = tabelas12022[2]
df1_12022.insert(0, "Sem_Ano", ["1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022",])
df2_12022.insert(0, "Sem_Ano", ["1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022","1_2022"])


m = pd.merge(df1_12022, df1_42021, how = 'outer')
m = pd.merge(m, df1_32021, how='outer')
m = pd.merge(m, df1_22021, how='outer')
m = pd.merge(m, df1_12021, how='outer')
m = pd.merge(m, df1_42020, how='outer')
m = pd.merge(m, df1_32020, how='outer')
m = pd.merge(m, df1_22020, how='outer')
m = pd.merge(m, df1_12020, how='outer')

n = pd.merge(df2_12022, df2_42021, how = 'outer')
n = pd.merge(n, df2_32021, how='outer')
n = pd.merge(n, df2_22021, how='outer')
n = pd.merge(n, df2_12021, how='outer')
n = pd.merge(n, df2_42020, how='outer')
n = pd.merge(n, df2_32020, how='outer')
n = pd.merge(n, df2_22020, how='outer')
n = pd.merge(n, df2_12020, how='outer')
 
m.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
m.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
m.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
m.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
m.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
m.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
m.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
m.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
m.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
m.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
m.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
m.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
m.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
m.drop('Ignorar', axis=1, inplace=True)
m.drop(0, axis=0, inplace=True)
m.drop(1, axis=0, inplace=True)
m.drop(11, axis=0, inplace=True)
m.drop(12, axis=0, inplace=True)

n.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
n.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
n.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
n.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
n.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
n.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
n.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
n.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
n.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
n.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
n.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
n.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
n.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
n.drop('Ignorar', axis=1, inplace=True)
n.drop(4, axis=0, inplace=True)
n.drop(9, axis=0, inplace=True)

m = pd.merge(m, n, how = 'outer')

Geral = ["Sem_Ano","Controle", "AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo", "Real_Estaca", "Potencial_Estaca"]
Alas = ["AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo"]
Estaca = ["Real_Estaca"]
Alas_Estaca = ["AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo", "Real_Estaca"]

Valores_alas = m.filter(items=Geral)
Valores_estacas = m.filter(items=Geral)

sl.title("Análise do Trimestral!")

#Filtrar Trimestres
base = Valores_alas.copy()
#sl.dataframe(base)
trimestre = base["Sem_Ano"].unique()
tri_selecionado = sl.multiselect("Selecione o Trimestre", trimestre)
base_new = base[base['Sem_Ano'].isin(tri_selecionado)]
sl.dataframe(base_new)

#Selecionar Gerar Gráficos
sl.header("Gerar Gráficos")
Controle = base["Controle"].unique()
Controle = sl.selectbox("Selecione o Indice", Controle)
base_controle = base[base['Controle'] == Controle]
#sl.dataframe(base_controle)

#Geração dos Gráficos
base_controle = base_controle.sort_index(ascending=False)
sl.dataframe(base_controle)
Alas_Estaca = base_controle.filter(items=Alas_Estaca)

# Definindo a variável do eixo x, que será o índice de uma das séries temporais
x = base_controle["Sem_Ano"].unique()

# Criando o objeto do gráfico
fig1 = go.Figure()

# Funções 'add_trace' para criar as linhas do gráfico
for i in Alas_Estaca:
    fig1.add_trace(go.Scatter(x=x, y=Alas_Estaca[i],
                            mode='markers+lines+text',
                            name=i,
                            text=Alas_Estaca[i],
                            textposition='top center'))              
                    
# Formatando o layout do gráfico
fig1.update_layout(title=Controle,
                   xaxis_title='Trimestre',
                   yaxis_title='Alas',
                   width=1000,
                   height=600)
                   
fig1.update_traces(textposition="top center")

# Exibindo o elemento do gráfico na página                
sl.plotly_chart(fig1)	
