import streamlit as sl
import matplotlib.pyplot as plt
import numpy as np
import tabula
import pandas as pd
import plotly as pl
import plotly.graph_objects as go
import plotly.express as px

pdf_path_12019 = ".\\Trimestrais\\1_2019.pdf"
pdf_path_22019 = ".\\Trimestrais\\2_2019.pdf"
pdf_path_32019 = ".\\Trimestrais\\3_2019.pdf"
pdf_path_42019 = ".\\Trimestrais\\4_2019.pdf"
pdf_path_12020 = ".\\Trimestrais\\1_2020.pdf"
pdf_path_22020 = ".\\Trimestrais\\2_2020.pdf"
pdf_path_32020 = ".\\Trimestrais\\3_2020.pdf"
pdf_path_42020 = ".\\Trimestrais\\4_2020.pdf"
pdf_path_12021 = ".\\Trimestrais\\1_2021.pdf"
pdf_path_22021 = ".\\Trimestrais\\2_2021.pdf"

tabelas12019 = tabula.read_pdf(pdf_path_12019, pages='1-2')
tabelas22019 = tabula.read_pdf(pdf_path_22019, pages='1-2')
tabelas32019 = tabula.read_pdf(pdf_path_32019, pages='1-2')
tabelas42019 = tabula.read_pdf(pdf_path_42019, pages='1-2')
tabelas12020 = tabula.read_pdf(pdf_path_12020, pages='1-2')
tabelas22020 = tabula.read_pdf(pdf_path_22020, pages='1-2')
tabelas32020 = tabula.read_pdf(pdf_path_32020, pages='1-2')
tabelas42020 = tabula.read_pdf(pdf_path_42020, pages='1-2')
tabelas12021 = tabula.read_pdf(pdf_path_12021, pages='1-2')
tabelas22021 = tabula.read_pdf(pdf_path_22021, pages='1-2')

#''' RELATORIO 3/2019 '''
tabelas32019_2 = tabelas32019[2]
tabelas32019_2 = tabelas32019_2[3:]
tabelas32019_1 = tabelas32019[1] 
tabelas32019_0 = tabelas32019[0]  
tabelas32019_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas32019_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas32019_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas32019_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas32019_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas32019_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas32019_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas32019_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas32019_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base3_2019 = pd.concat([tabelas32019_1, tabelas32019_2], ignore_index=True)
base3_2019 = pd.concat([tabelas32019_0, base3_2019], ignore_index=True)
base3_2019.insert(0, "Sem_Ano", ["3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019", "3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019", "3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019","3_2019"])

#''' RELATORIO 4/2019 '''
tabelas42019_2 = tabelas42019[2]
tabelas42019_2 = tabelas42019_2[3:]
tabelas42019_1 = tabelas42019[1] 
tabelas42019_0 = tabelas42019[0]  
tabelas42019_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas42019_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas42019_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas42019_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas42019_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas42019_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas42019_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas42019_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas42019_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base4_2019 = pd.concat([tabelas42019_1, tabelas42019_2], ignore_index=True)
base4_2019 = pd.concat([tabelas42019_0, base4_2019], ignore_index=True)
base4_2019.insert(0, "Sem_Ano", ["4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019", "4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019", "4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019","4_2019"])

#''' RELATORIO 1/2020 '''
tabelas12020_2 = tabelas12020[2]
tabelas12020_2 = tabelas12020_2[3:]
tabelas12020_1 = tabelas12020[1] 
tabelas12020_0 = tabelas12020[0]  
tabelas12020_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas12020_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas12020_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas12020_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas12020_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas12020_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas12020_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas12020_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas12020_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base1_2020 = pd.concat([tabelas12020_1, tabelas12020_2], ignore_index=True)
base1_2020 = pd.concat([tabelas12020_0, base1_2020], ignore_index=True)
base1_2020.insert(0, "Sem_Ano", ["1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020", "1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020", "1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020","1_2020"])

#''' RELATÓRIO 2/2020 '''
tabelas22020_2 = tabelas22020[2]
tabelas22020_2 = tabelas22020_2[3:]
tabelas22020_1 = tabelas22020[1] 
tabelas22020_0 = tabelas22020[0]  
tabelas22020_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas22020_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas22020_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas22020_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas22020_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas22020_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas22020_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas22020_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas22020_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base2_2020 = pd.concat([tabelas22020_1, tabelas22020_2], ignore_index=True)
base2_2020 = pd.concat([tabelas22020_0, base2_2020], ignore_index=True)
base2_2020.insert(0, "Sem_Ano", ["2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020", "2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020", "2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020","2_2020"])


#''' RELATÓRIO 3/2020 '''
tabelas32020_2 = tabelas32020[2]
tabelas32020_2 = tabelas32020_2[3:]
tabelas32020_1 = tabelas32020[1] 
tabelas32020_0 = tabelas32020[0]  
tabelas32020_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas32020_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas32020_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas32020_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas32020_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas32020_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas32020_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas32020_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas32020_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base3_2020 = pd.concat([tabelas32020_1, tabelas32020_2], ignore_index=True)
base3_2020 = pd.concat([tabelas32020_0, base3_2020], ignore_index=True)
base3_2020.insert(0, "Sem_Ano", ["3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020", "3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020", "3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020","3_2020"])

#''' RELATÓRIO 4/2020 '''
tabelas42020_2 = tabelas42020[2]
tabelas42020_2 = tabelas42020_2[3:]
tabelas42020_1 = tabelas42020[1] 
tabelas42020_0 = tabelas42020[0]  
tabelas42020_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas42020_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas42020_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas42020_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas42020_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas42020_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas42020_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas42020_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas42020_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base4_2020 = pd.concat([tabelas42020_1, tabelas42020_2], ignore_index=True)
base4_2020 = pd.concat([tabelas42020_0, base4_2020], ignore_index=True)
base4_2020.insert(0, "Sem_Ano", ["4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020", "4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020", "4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020","4_2020", "4_2020"])


#''' RELATÓRIO 1/2021 '''
tabelas12021_2 = tabelas12021[2]
tabelas12021_2 = tabelas12021_2[3:]
tabelas12021_1 = tabelas12021[1] 
tabelas12021_0 = tabelas12021[0]  
tabelas12021_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas12021_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas12021_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas12021_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas12021_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas12021_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas12021_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas12021_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas12021_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base1_2021 = pd.concat([tabelas12021_1, tabelas12021_2], ignore_index=True)
base1_2021 = pd.concat([tabelas12021_0, base1_2021], ignore_index=True)
base1_2021.insert(0, "Sem_Ano", ["1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021", "1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021", "1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021","1_2021", "1_2021"])


#''' RELATÓRIO 1/2021 '''
tabelas22021_2 = tabelas22021[2]
tabelas22021_2 = tabelas22021_2[3:]
tabelas22021_1 = tabelas22021[1] 
tabelas22021_0 = tabelas22021[0]  
tabelas22021_0.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas22021_0.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas22021_0.rename(columns={'Total da Estaca': 'Casca3'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 5': 'Ignorar'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 6': 'Real_Estaca'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 7': 'Potencial_Estaca'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 8': '2021'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 9': '2020'}, inplace=True)
tabelas22021_0.rename(columns={'Unnamed: 10': '2016'}, inplace=True)
tabelas22021_1.rename(columns={'Membros/Famílias': 'Controle'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 0': 'AltAlg'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 1': 'Casca1'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 2': 'Casca3'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 3': 'Coquei'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 4': 'Paloti'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 5': 'Toledo'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 6': 'Ignorar'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 7': 'Real_Estaca'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 8': 'Potencial_Estaca'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 9': '2021'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 10': '2020'}, inplace=True)
tabelas22021_1.rename(columns={'Unnamed: 11': '2016'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 0': 'Controle'}, inplace=True)
tabelas22021_2.rename(columns={'Ala/Ramo Real': 'AltAlg'}, inplace=True)
tabelas22021_2.rename(columns={'Total da Estaca': 'Casca1'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 1': 'Casca3'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 2': 'Coquei'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 3': 'Paloti'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 4': 'Toledo'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 5': 'Real_Estaca'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 6': 'Potencial_Estaca'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 7': '2021'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 8': '2020'}, inplace=True)
tabelas22021_2.rename(columns={'Unnamed: 9': '2016'}, inplace=True)

base2_2021 = pd.concat([tabelas22021_1, tabelas22021_2], ignore_index=True)
base2_2021 = pd.concat([tabelas22021_0, base2_2021], ignore_index=True)
base2_2021.insert(0, "Sem_Ano", ["2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021", "2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021", "2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021","2_2021", "2_2021"])


base_total = pd.concat([base3_2019, 
                        base4_2019, 
                        base1_2020, 
                        base2_2020, 
                        base3_2020,
                        base4_2020,
                        base1_2021,
                        base2_2021], ignore_index=True)
#m.drop('Ignorar', axis=1, inplace=True)
#m.drop(0, axis=0, inplace=True)
#m.drop(1, axis=0, inplace=True)
#m.drop(11, axis=0, inplace=True)
#m.drop(12, axis=0, inplace=True)
filtro  = base_total['AltAlg'].notnull()
base_total = base_total[filtro]

Geral = ["Sem_Ano","Controle", "AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo", "Real_Estaca", "Potencial_Estaca"]
Alas = ["AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo"]
Estaca = ["Real_Estaca"]
Alas_Estaca = ["AltAlg", "Casca1", "Casca3", "Coquei", "Paloti", "Toledo", "Real_Estaca"]

Valores_alas = base_total.filter(items=Geral)
Valores_estacas = base_total.filter(items=Geral)

sl.title("Análise do Trimestral!")

#Filtrar Trimestres
base = Valores_alas.copy()
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
base_controle = base_controle.sort_index(ascending=True)
#sl.dataframe(base_controle)
Alas_Estaca = base_controle.filter(items=Alas_Estaca)

# Definindo a variável do eixo x, que será o índice de uma das séries temporais
x = base_controle["Sem_Ano"].unique()

# Criando o objeto do gráfico
fig1 = go.Figure()

# Funções 'add_trace' para criar as linhas do gráfico
for i in Alas_Estaca:
    fig1.add_trace(go.Scatter(x=x, y=Alas_Estaca[i],
                            mode='markers+lines',
                            name=i))              
                    
# Formatando o layout do gráfico
fig1.update_layout(title=Controle,
                   xaxis_title='Trimestre',
                   yaxis_title='Alas',
                   width=1000,
                   height=600)

# Exibindo o elemento do gráfico na página                
sl.plotly_chart(fig1)	