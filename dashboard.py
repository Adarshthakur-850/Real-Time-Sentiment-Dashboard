import streamlit as st 
import pandas as pd 
import plotly .express as px 
import plotly .graph_objects as go 
from streamlit_autorefresh import st_autorefresh 
import os 
from wordcloud import WordCloud 
import matplotlib .pyplot as plt 

st .set_page_config (page_title ="Sentiment Dashboard",layout ="wide")


st_autorefresh (interval =2000 ,key ="datarefresh")

DATA_FILE ="data/tweets.csv"

def load_data ():
    if not os .path .exists (DATA_FILE ):
        return pd .DataFrame (columns =['timestamp','text','sentiment','score','keyword'])
    try :
        return pd .read_csv (DATA_FILE )
    except :
        return pd .DataFrame ()

st .title ("📊 Real-Time Twitter Sentiment Dashboard")

col1 ,col2 =st .columns ([1 ,3 ])

df =load_data ()

with col1 :
    st .subheader ("Filters")
    if not df .empty :
        keywords =['All']+list (df ['keyword'].unique ())
        selected_kw =st .selectbox ("Select Keyword",keywords )

        if selected_kw !='All':
            df =df [df ['keyword']==selected_kw ]

    st .info ("Run `src/streamer.py` to generate live data.")


m1 ,m2 ,m3 ,m4 =st .columns (4 )
total =len (df )
pos =len (df [df ['sentiment']=='Positive'])
neg =len (df [df ['sentiment']=='Negative'])
neu =len (df [df ['sentiment']=='Neutral'])

m1 .metric ("Total Tweets",total )
m2 .metric ("Positive",pos ,delta =f"{pos /total *100 :.1f}%"if total >0 else "0%")
m3 .metric ("Negative",neg ,delta =f"-{neg /total *100 :.1f}%"if total >0 else "0%")
m4 .metric ("Neutral",neu )


c1 ,c2 =st .columns (2 )

with c1 :
    st .subheader ("Sentiment Distribution")
    if total >0 :
        fig =px .pie (df ,names ='sentiment',color ='sentiment',
        color_discrete_map ={'Positive':'green','Negative':'red','Neutral':'gray'})
        st .plotly_chart (fig ,use_container_width =True )

with c2 :
    st .subheader ("Sentiment Over Time")
    if total >0 :


        df ['idx']=range (len (df ))
        fig =px .line (df .tail (100 ),x ='idx',y ='score',color ='sentiment',markers =True )
        st .plotly_chart (fig ,use_container_width =True )


st .subheader ("Word Cloud")
if total >0 :
    text =" ".join (df ['text'].tolist ())
    wc =WordCloud (width =800 ,height =400 ,background_color ='black').generate (text )
    plt .figure (figsize =(10 ,5 ))
    plt .imshow (wc ,interpolation ='bilinear')
    plt .axis ("off")
    st .pyplot (plt )


st .subheader ("Recent Live Tweets")
if total >0 :
    st .dataframe (df .tail (10 )[['timestamp','sentiment','text','keyword']].iloc [::-1 ],use_container_width =True )
