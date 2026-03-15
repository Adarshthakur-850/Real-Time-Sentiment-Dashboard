from fastapi import FastAPI 
from fastapi .middleware .cors import CORSMiddleware 
import pandas as pd 
import os 

app =FastAPI (title ="Sentiment API")

app .add_middleware (
CORSMiddleware ,
allow_origins =["*"],
allow_methods =["*"],
allow_headers =["*"],
)

DATA_FILE ="data/tweets.csv"

@app .get ("/")
def home ():
    return {"status":"active","message":"Sentiment Analysis API"}

@app .get ("/stats")
def get_stats ():
    if not os .path .exists (DATA_FILE ):
        return {"error":"No data available"}

    try :
        df =pd .read_csv (DATA_FILE )
        stats =df ['sentiment'].value_counts ().to_dict ()
        total =len (df )
        return {"total":total ,"distribution":stats }
    except Exception as e :
        return {"error":str (e )}

@app .get ("/tweets")
def get_tweets (limit :int =10 ):
    if not os .path .exists (DATA_FILE ):
        return []

    try :
        df =pd .read_csv (DATA_FILE )

        return df .tail (limit ).to_dict (orient ='records')[::-1 ]
    except :
        return []
