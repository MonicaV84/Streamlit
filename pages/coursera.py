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

url_coursera = 'https://drive.google.com/file/d/1augQGT2oCGB9x9wY_-xVOkYxbZXkCrlW/view?usp=sharing'
path_coursera = 'https://drive.google.com/uc?export=download&id='+url_coursera.split('/')[-2]
@st.cache
def read_coursera():
    coursera = pd.read_csv(path_coursera)
    return coursera
df_coursera = read_coursera()


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



reviews_per_year = df_kpi['compound'].value_counts().sum()




st.subheader('Reviews por año')
reviews_per_year = st.header(f'{reviews_per_year :,.0f}')



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





