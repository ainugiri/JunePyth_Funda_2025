import nltk
nltk.download('punkt')
nltk.download('stopwords', force=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print("Lemmatization Example:")
word = "better" 
print("Original Word:", word)
print(lemmatizer.lemmatize(word, pos='a'))  # 'a' for adjective

print("Tokenization Example:")
word = "Executing"
print("Original Word:", word)
print("lemmatized Word:", lemmatizer.lemmatize(word.lower(), pos='v'))  # 'v' for verb

text = "NLP with Python is better to learn"
tokens = text.split()
print("Tokens:", tokens)
# [NLP, with, Python, is, good, to, learn]
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)
# [NLP, Python, good, learn]
# NLU
#1.  intent recognition
# Siri, set an alarm for 7 AM -> intent: set_alarm, 
#2.  entity recognition
# Extracting entities like time, date, etc.entities: {time: 7 AM}
#3.  sentiment analysis
# I love this product! -> sentiment: positive
# It is not so tasty -> sentiment: negative
# It is okay -> sentiment: neutral
# 4.  text classification
# Classifying text into categories like spam, ham, etc.
# cancel my flight -> intent: cancel_flight -> category: travel
# cancel my subscription -> intent: cancel_subscription -> category: subscription

# NLU -> Alexa, Siri, Assistant, ChatGPT, etc. 


# NLG
# Generating human-like text based on input..
# 1. Content Planning -> what to write about
# 2. Sentence Planning -> how to organize the content
# 3. Surface Realization -> generating the actual text
# 4. Text Generation -> using models like GPT-3, BERT, etc. 

# GPT - Generative Pre-trained Transformer
# BERT - Bidirectional Encoder Representations from Transformers
# T5 - Text-to-Text Transfer Transformer


