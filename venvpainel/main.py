import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Relatórios')
st.subheader('**Classificação **')
uploaded_file = st.file_uploader("Procurar arquivo", type="xlsx")


if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if st.sidebar.checkbox("Tabela"):
        st.header("Dados:")
        st.write(df)
        st.table(df)

    if st.sidebar.checkbox("Dados "):
        st.header("Dados:")
        st.dataframe(df)

    if st.sidebar.checkbox("Gráfico "):
        st.header("Dados:")
        st.bar_chart(df)



df = pd.read_excel("C:\\Users\Richielly\Downloads\\relatorio_ferias_19012021223955.xlsx")

valores = df['Inicio']

st.write(valores)
st.bar_chart(valores)

coluna = st.multiselect('Colunas', df.columns)
st.multiselect('Valores', df.values[1])


texto = st.text_input('Altura','200')
texto = st.slider('Slide me', min_value=100, max_value=600)
st.bar_chart(df,100,int(texto))

progress = st.slider('Progresso', min_value=1, max_value=100)
st.progress(progress)
if progress == 100:
    st.spinner()
    with st.spinner(text='Corrida...'):
        time.sleep(5)
        st.success('Terminou')
        st.balloons()

    st.color_picker('Aquarela')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')

