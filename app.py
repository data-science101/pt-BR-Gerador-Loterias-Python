import streamlit as st
import random

css_styles = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(css_styles, unsafe_allow_html=True)

st.title('Gerador de números Loterias Caixa')
st.write('Jogos disponíveis: Mega-Sena, Lotofácil, Quina, Lotomania e Dia de Sorte.')

# Input de variáveis para o gerador
tipo = st.selectbox(
     'Qual jogo da loteria deseja gerar as apostas?',
     ('Mega-Sena', 'Lotofácil', 'Quina', 'Lotomania', 'Dia de Sorte'))
jogos = st.number_input('Quantidade de apostas:', step=1)
budget = st.number_input('Qual o seu orçamento? R$', step=5)
v_jogo = st.number_input('Qual o valor de cada aposta? R$', step=0.5)

max_apostas = 0
cont = 0
num_apostas = 0

try:
    max_apostas = budget / v_jogo
    max_apostas = max_apostas.__floor__()
except:
    pass
    #

# Lista de meses para o jogo Dia de Sorte
meses_sorte = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
               'Novembro', 'Dezembro']

st.info('Você consegue realizar {} apostas com o seu orçamento de R${}.'.format(max_apostas, budget))

with st.container():

    # Apostas Mega-Sena
    if tipo == 'Mega-Sena':
        num_apostas = st.slider('Quantidade de números de cada aposta:', 6, 15, 6)
        for i in range(0, jogos):
            cont = cont + 1
            gerador = random.sample(range(1, 61), k=num_apostas)
            gerador.sort()
            st.write('Aposta {}: {}'.format(cont, gerador))
            if i == max_apostas - 1:
                st.warning('Quantidade máxima de apostas atingida pelo seu orçamento.')
                break

    # Apostas Lotofácil
    if tipo == 'Lotofácil':
        num_apostas = st.slider('Quantidade de números de cada aposta:', 15, 20, 15)
        for i in range(0, jogos):
            cont = cont + 1
            gerador = random.sample(range(1, 26), k=num_apostas)
            gerador.sort()
            st.write('Aposta {}: {}'.format(cont, gerador))
            if i == max_apostas - 1:
                st.warning('Quantidade máxima de apostas atingida pelo seu orçamento.')
                break

    # Apostas Quina
    if tipo == 'Quina':
        num_apostas = st.slider('Quantidade de números de cada aposta:', 5, 15, 5)
        for i in range(0, jogos):
            cont = cont + 1
            gerador = random.sample(range(1, 81), k=num_apostas)
            gerador.sort()
            st.write('Aposta {}: {}'.format(cont, gerador))
            if i == max_apostas - 1:
                st.warning('Quantidade máxima de apostas atingida pelo seu orçamento.')
                break

    # Apostas Lotomania
    if tipo == 'Lotomania':
        for i in range(0, jogos):
            cont = cont + 1
            gerador = random.sample(range(1, 101), k=50)
            gerador.sort()
            st.write('Aposta {}: {}'.format(cont, gerador))
            if i == max_apostas - 1:
                st.warning('Quantidade máxima de apostas atingida pelo seu orçamento.')
                break

    # Apostas Dia de Sorte
    if tipo == 'Dia de Sorte':
        num_apostas = st.slider('Quantidade de números de cada aposta:', 7, 15, 7)
        for i in range(0, jogos):
            cont = cont + 1
            gerador = random.sample(range(1, 32), k=num_apostas)

            # Gerando mês aleatório baseado na lista criada no início
            gerador_sorte = random.choice(meses_sorte)
            gerador.sort()
            st.write('Aposta {}: {}  Mês da sorte: {}.'.format(cont, gerador, gerador_sorte))
            if i == max_apostas - 1:
                st.warning('Quantidade máxima de apostas atingida pelo seu orçamento.')
                break


st.write("Criado por [DS 101](https://github.com/data-science101).")
