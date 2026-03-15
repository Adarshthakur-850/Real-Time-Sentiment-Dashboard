import nltk 
from nltk .sentiment .vader import SentimentIntensityAnalyzer 


try :
    nltk .data .find ('sentiment/vader_lexicon.zip')
except LookupError :
    nltk .download ('vader_lexicon',quiet =True )

class SentimentAnalyzer :
    def __init__ (self ):
        self .sia =SentimentIntensityAnalyzer ()

    def analyze (self ,text ):
        score =self .sia .polarity_scores (text )
        compound =score ['compound']

        if compound >=0.05 :
            label ='Positive'
        elif compound <=-0.05 :
            label ='Negative'
        else :
            label ='Neutral'

        return {
        'label':label ,
        'score':compound ,
        'details':score 
        }
