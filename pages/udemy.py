
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Configuración de la página

st.set_page_config(
    page_title='Udemy',
    layout='wide'

)


# importo los csv que voy a utilizar desde Google Drive

# CSV de UDEMY 

url_udemy = 'https://drive.google.com/file/d/1PFW3LeJe7C3b6WptTixbsluHDDQqDr_6/view?usp=sharing'
path_udemy = 'https://drive.google.com/uc?export=download&id='+url_udemy.split('/')[-2]

@st.cache # guarda a caché para que no demore la carga
def read_udemy():
    udemy = pd.read_csv(path_udemy)
    return udemy
df_udemy = read_udemy()
  
 
 
st.image('./udemy_logo.png', width=150)

st.markdown('---')
 
# --- VISUALIZACIÓN --- #
st.sidebar.header("Seleccione los criterios para visualizar KPI's")
# --- KPI's --- #

anio = st.sidebar.multiselect(
    'Seleccione el año',
    options=df_udemy['year'].unique(),
    default=[2017]
)
tema = st.sidebar.multiselect(
    'Seleccione el tema',
    options=df_udemy['subject'].unique(),
    default=df_udemy['subject'].unique()
)
if tema == []:
    st.warning('Seleccione al menos una opción')

nivel = st.sidebar.multiselect(
    'Seleccione el nivel',
    options=df_udemy['level'].unique(),
    default=df_udemy['level'].unique()
)
if nivel == []:
    st.warning('Seleccione al menos una opción')

# --- Defino los criterios de filtrado para los KPI's --- #

df_kpi = df_udemy.query(
    "year == @anio & subject == @tema & level == @nivel " 
)

total_sales = (df_kpi['price']* df_kpi['num_subscribers']).sum()
average_sales_by_year =round((df_kpi.price).mean(),2)
students_per_year = df_kpi['num_subscribers'].sum()

left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Ventas por año')
    st.header(f'${total_sales :,.0f}')

with middle_column:
    st.subheader('Estudiantes por año')
    st.header(f'{students_per_year :,.0f}')

with right_column:
    st.subheader('Precio promedio')
    average =st.header(f'${average_sales_by_year}')


st.markdown('---')





# --- barchart --- #

groupby_column = st.selectbox(
    '¿Qué datos desea analizar?',
    ('level', 'year', 'subject', 'num_lectures','content_duration')
)

output_column = ['price', 'num_subscribers']
df_grouped = df_udemy.groupby(by=[groupby_column], as_index=False)[output_column].sum()

fig = px.bar(
    df_grouped,
    x=groupby_column,
    y='price',
    color='num_subscribers',
    template='seaborn',
    width=800,
    height=550,
    title= f'<b>Suma del precio y el número de suscriptores por {groupby_column}</b>'    
)
st.plotly_chart(fig)

# --- Wordcloud --- #

st.set_option('deprecation.showPyplotGlobalUse', False)


text = df_udemy['course_title'].values

w = WordCloud().generate(str(text))
plt.imshow(w, interpolation='bilinear')
plt.axis("off")
plt.show()

agree = st.checkbox('Mostrar nube de palabras')

if agree:
    
     st.pyplot()












