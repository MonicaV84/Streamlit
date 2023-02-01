import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(
    page_title='Edx',
    layout='wide'

)

# CSV de EDX
url_edx = 'https://drive.google.com/file/d/1qHA8ivOQAV63i1fA9aHAvDEgAYeM2Xsv/view?usp=share_link'
path_edx = 'https://drive.google.com/uc?export=download&id='+url_edx.split('/')[-2]

@st.cache
def read_edx():
    edx = pd.read_csv(path_edx)
    return edx
read_edx()
df_edx = read_edx()

# --- Logo --- #

st.image('./edx_logo.jpg', width=150)

st.markdown('---')


# --- KPI's --- #
st.sidebar.header("Seleccione los criterios para visualizar KPI's")

idioma = st.sidebar.multiselect(
    'Seleccione el idioma',
    options=df_edx['language'].unique(),
    default=['English']
    
)

tema1 = st.sidebar.multiselect(
    'Seleccione el tema',
    options=df_edx['subject'].unique(),
    default=['Computer Science']
    
)


nivel1 = st.sidebar.multiselect(
    'Seleccione el nivel',
    options=df_edx['Level'].unique(),
    default=['Introductory']
    
)


carga_horaria = st.sidebar.multiselect(
    'Seleccione la carga horaria',
    options=df_edx['course_effort'].unique(),
    default=['2–3 hours per week']
    
)

df_kpi1 = df_edx.query(
    "course_effort == @carga_horaria & subject == @tema1 & Level == @nivel1 " 
)

ventas_totales = (df_kpi1.certification_value * df_kpi1.n_enrolled).sum()
promedio_ventas_anual =round((df_kpi1.certification_value).mean(),2)
estudiantes_por_anio = df_kpi1['n_enrolled'].sum()

left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Ventas por año')
    st.header(f'${ventas_totales :,.0f}')

with middle_column:
    st.subheader('Estudiantes por año')
    st.header(f'{estudiantes_por_anio :,.0f}')

with right_column:
    st.subheader('Precio promedio')
    average =st.header(f'${promedio_ventas_anual}')

st.markdown('---')





# --- Criterios de selección del gráfico de barras --- #




groupby_column = st.sidebar.radio(
            '¿Qué datos desea analizar?',
            options=('Level', 'language', 'course_type', 'course_length', 'course_effort', 'subject')
)


# --- Columnas que voy a usar para evaluar los criterios de selección --- #


output_column = ['certification_value', 'n_enrolled']
df_grouped = df_edx.groupby(by=[groupby_column], as_index=False)[output_column].sum()

# --- Ploteo --- #

fig = px.bar(
    df_grouped,
    x=groupby_column,
    y='certification_value',
    color='n_enrolled',
    template='ggplot2',
    height=550,
    title= f'<b>Suma del precio y el número de inscriptos por {groupby_column}</b>'
)
st.plotly_chart(fig)



# --- Wordcloud --- #

st.set_option('deprecation.showPyplotGlobalUse', False) # Impide que se muestren warnings en la app

text = df_edx['title'].values

w = WordCloud().generate(str(text))
plt.imshow(w, interpolation='bilinear')
plt.axis("off")
plt.show()

agree1 = st.checkbox('Mostrar nube de palabras')

if agree1:
    
     st.pyplot()
















