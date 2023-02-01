import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(
    page_title='coursera',
    layout='wide'

)

# cv Coursera
@st.cache
def read():

    df_coursera = pd.read_csv('/home/monica/moocs_data_analysis/.venv/coursera_final.csv')
    return df_coursera
read()
df_coursera = read()

st.image('./coursera_logo.png', width=150)

st.markdown('---')

anio2 = st.sidebar.multiselect(
    'Seleccione el año',
    options=df_coursera['year'].unique(),
    default=[2020]
)




df_kpi = df_coursera.query(
    "year == @anio2 " 
)


average_compound =round((df_kpi.compound).mean(),2)
reviews_per_year = df_kpi['reviewers'].sum()

left_column,right_column= st.columns(2)
with left_column:
    st.subheader('Promedio de compound')
    st.header(f'${average_compound :,.0f}')


with right_column:
    st.subheader('Reviews por año')
    average =st.header(f'${reviews_per_year}')


st.markdown('---')


st.set_option('deprecation.showPyplotGlobalUse', False)


fig = px.histogram(df_coursera, x="rating")

st.plotly_chart(fig)

fig1 = px.histogram(df_coursera, x="sentiment")
st.plotly_chart(fig1)


text = df_coursera['name'].values

w = WordCloud().generate(str(text))
plt.imshow(w, interpolation='bilinear')
plt.axis("off")
plt.show()

agree2 = st.checkbox('Mostrar nube de palabras')
if agree2:
    
     st.pyplot()





