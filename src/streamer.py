import time 
import pandas as pd 
import os 
import random 
from datetime import datetime 
from src .sentiment import SentimentAnalyzer 

DATA_FILE ="data/tweets.csv"

class TweetStreamer :
    def __init__ (self ):
        self .analyzer =SentimentAnalyzer ()
        self ._init_storage ()

    def _init_storage (self ):
        if not os .path .exists ("data"):
            os .makedirs ("data")
        if not os .path .exists (DATA_FILE ):
            df =pd .DataFrame (columns =['timestamp','text','sentiment','score','keyword'])
            df .to_csv (DATA_FILE ,index =False )

    def save_tweet (self ,text ,keyword ):
        result =self .analyzer .analyze (text )

        new_data ={
        'timestamp':datetime .now ().strftime ("%Y-%m-%d %H:%M:%S"),
        'text':text ,
        'sentiment':result ['label'],
        'score':result ['score'],
        'keyword':keyword 
        }


        df =pd .DataFrame ([new_data ])
        df .to_csv (DATA_FILE ,mode ='a',header =False ,index =False )
        print (f"[{result ['label']}] {text [:50 ]}...")

    def start_mock_stream (self ):
        print ("Starting Mock Stream... (Press Ctrl+C to stop)")
        keywords =['#AI','#Tech','#Crypto','#Python','#Startup']

        templates =[
        "I love usage of {}! It's amazing.",
        "{} is failing hard today. Terrible performance.",
        "Just checking out {}, seems okay.",
        "Why is {} so popular? I don't get the hype.",
        "Investing in {} is the best decision I made.",
        "{} broken again. Please fix it.",
        "Excited for the new {} update!",
        "Neutral opinion on {}, wait and see."
        ]

        try :
            while True :
                kw =random .choice (keywords )
                text =random .choice (templates ).format (kw )
                self .save_tweet (text ,kw )
                time .sleep (random .uniform (1 ,3 ))
        except KeyboardInterrupt :
            print ("Stream stopped.")

if __name__ =="__main__":
    streamer =TweetStreamer ()
    streamer .start_mock_stream ()
