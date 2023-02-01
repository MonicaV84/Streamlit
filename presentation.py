import streamlit as st
st.set_page_config(
    page_title='Moocs',
    layout='wide'

)
st.markdown('# ¡Bienvenidos a esta presentación!')
st.image('mooc.jpg')
st.subheader('Objetivos')
lst = ['Analizar métricas para determinar cuánto influyen en las ventas', 'Determinar KPIs', 'Exponer conclusiones']

s = ''

for i in lst:
    s += "- " + i + "\n"

st.markdown(s)