#implement sentiment analysis 

#pip install nltk
#pip install vader lexicon (sentiment scores purpose)

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

#initialise sentiment analyser 
sid = SentimentIntensityAnalyzer()

#sample text
text = "In this example, we utilize Python to perform sentiment analysis on textual data. By leveraging the VADER lexicon from NLTK, we can assess the sentiment of a given piece of text. After initializing the sentiment analyzer, we provide a sample text for analysis. The analyzer computes sentiment scores, including positive, negative, neutral, and compound scores. These scores offer insights into the overall sentiment expressed in the text. By interpreting the compound score, we classify the sentiment as positive, negative, or neutral. This straightforward implementation enables us to quickly evaluate the sentiment of text data, making it useful for various applications such as social media monitoring, customer feedback analysis, and opinion mining. "

#performing sentiment analysis
sentiment_scores = sid.polarity_scores(text)

#print sentiment scores
print(sentiment_scores)

#interpret sentiment scores 
if sentiment_scores['compound'] >= 0.05 :
    print("Postive Sentiment")
elif sentiment_scores['compound'] <= -0.05 :
    print("Negative Sentiments")
else :
    print("Neutral Sentiment")

