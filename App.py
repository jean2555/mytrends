
from time import time
import time
import pandas as pd
import streamlit as st
from subprocess import call
import plotly.express as px
import json



st.set_page_config(
    page_title="My Trends",
    page_icon="🖐️",
    layout='wide',)


st.sidebar.header("Bienvenue chez")


# integrer des icones

st.title('Main')
st.sidebar.markdown("Author: Jean Olivier")
st.sidebar.markdown("<div><img src='https://pngfolio.com/images/all_img/copy/1645074099tiktok%20rgb.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown(
    "Ce tableau de bord va vous aide creer votre video virale.")
st.sidebar.markdown(
    " Pour commencer <ol><li> Entrer un  <i>hashtag</i> que vous souhaitez ananlyser</li> <li>Appuyer sur le bouton <i>Get Data</i>.</li> <li> Obtenez votre analyse</li></ol>", unsafe_allow_html=True)

stats = {}
id = dict()

st.info('Cliquer à deux reprises sur le bouton pour me réveiller !', icon="😪")

with open('export.json', 'r') as f:
    data = json.load(f)

 # statistique de count

    for key in data.keys():
        stats[key] = data[key]['stats']
        id[key] = data[key]['id']
    con_lis = list(id.items())    
    de = pd.DataFrame.from_dict(stats, orient='index')
    de['id'] = con_lis
    

 # input
    hashtag = st.text_input('Entrer un hashtag ', value='')
 # recupérer la données

    if st.button('Get Data'):

        st.write(hashtag)
        call(['python', 'tik.py', hashtag])
    #df1 = pd.read_csv('tiktokdata.csv')

    #df.to_csv('tiktokdata.csv', index=True, header=True)
    #df = pd.read_csv('tiktokdata.csv')
    #df = df.T
        with st.spinner('Wait for it...'):
            time.sleep(5)
            st.success('Reussite!')

 # plotly viz here
 # so=df.iloc[2]['authorStats']
        di = pd.DataFrame.from_dict(data, orient='index', columns=['id', 'desc', 'authorStats', 'stats', 'music'])
        di

 # figures

        fig = px.histogram(de, x= 'id', y='diggCount', width=800, height=400,title="Nombre de like générer par votre mots")
        st.plotly_chart(fig, use_container_width=False)


 # Split columns
        left_col, right_col = st.columns(2)

 # First Chart - video stats
        scatter1 = px.scatter(de, x='diggCount',
                              y='commentCount', width=800, height=400, title="indices des commentaires des utilisateurs")
        left_col.plotly_chart(scatter1, use_container_width=False)

 # Second Chart
        scatter2 = px.scatter(di, x='id', y='desc', width=800, height=400)
        scatter2

    # Split columns
    left_col, right_col = st.columns(2)

   # First Chart - video stats
    scatter1 = px.scatter(de, x='id', y='playCount', hover_data=[
                          'id'], size='playCount', color='playCount', title='Comments and Shares information', labels={'shareCount': '# Shares', 'commentCount': '# Comments'})
    left_col.plotly_chart(scatter1, use_container_width=False)

 
 
