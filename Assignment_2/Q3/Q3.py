
import nltk 

from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.stem import *
from nltk.stem.porter import PorterStemmer
import operator
import re
import string
import matplotlib
import matplotlib.pyplot as plt


imdb = ""
amazon = ""
yelp = ""


with open ('imdb_labelled.txt') as f:
    imdb = f.read()
with open ('amazon_cells_labelled.txt') as f:
    amazon = f.read()
with open ('yelp_labelled.txt') as f:
    yelp = f.read()

imdb_tokens = nltk.wordpunct_tokenize(imdb)
amazon_tokens = nltk.wordpunct_tokenize(amazon)
yelp_tokens = nltk.wordpunct_tokenize(yelp)


## (used in freq dist plot) This removes puntuation and lowers the alphabets 
imdb_vocab = list(sorted((map(lambda w : (re.sub(r'[\W]', '', w)).lower(), imdb_tokens))))
amazon_vocab = list(sorted((map(lambda w : (re.sub(r'[\W]', '', w)).lower(), amazon_tokens))))
yelp_vocab = list(sorted((map(lambda w : (re.sub(r'[\W]', '', w)).lower(), yelp_tokens))))


imdb_freq = FreqDist(imdb_vocab)
amazon_freq = FreqDist(amazon_vocab)
yelp_freq = FreqDist(yelp_vocab)


tokens = (nltk.wordpunct_tokenize(imdb + amazon + yelp))
text = nltk.Text(tokens)
words = [w.lower() for w in text]
vocab = sorted(set(words))
len(vocab)

## remove stop words 
vocab = [w for w in vocab if w not in stopwords.words('english')]
# stopwords
len(vocab)


# 5268 - 5128 


# ### Removing punctuation...
# Note that as the instructor suggested, I'm removing puntuation as part of preprocessing.

vocab = list(sorted(set(map(lambda w : re.sub(r'[\W]', '', w), vocab))))
len(vocab)


# ### Lemmatization...


wnl = WordNetLemmatizer()
lemmatized_vocab = list(set(map(lambda w : wnl.lemmatize(w), vocab)))
len(lemmatized_vocab)


# ### Stemming...

porter_stemmer = PorterStemmer()
stemmed_lemmatized_vocab = list(set(map(lambda w : porter_stemmer.stem(w), lemmatized_vocab)))
len(stemmed_lemmatized_vocab)


# ### Vocab size after preprocessing is 3960; Size before preprocessing was 5268.  $Difference $:


# 5268 - 3960

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sentiment = (sid.polarity_scores('amazing'))
(max(sentiment.items(), key=operator.itemgetter(1))[0]) 

def top_pos_neg_words(word_freq):
    imdb_positive_words = {}
    imdb_negative_words = {}
    # imdb_freq = dict(imdb_freq)
    for word,count in word_freq.items():
        if (len(imdb_negative_words) >= 10 and len(imdb_positive_words) >= 10):
            break
        if (len(word) > 1):
            sentiment = sid.polarity_scores(word)
            dom_sent = (max(sentiment.items(), key=operator.itemgetter(1))[0]) 
            if dom_sent == 'neg':
#                 if (len(imdb_negative_words) < 10):
                    imdb_negative_words[word] = count
            if dom_sent == 'pos':
#                 if (len(imdb_positive_words) < 10):
                    imdb_positive_words[word] = count
    return imdb_positive_words, imdb_negative_words

domains = [yelp_freq, imdb_freq, amazon_freq]

for word_freq in domains:
    print(top_pos_neg_words(word_freq))

pos, neg = (top_pos_neg_words(yelp_freq))
plt.bar (list(pos.keys()), list(pos.values()), width = .3)
labels = (list(pos.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('Yelp Most Used Positive Words', loc='center')
plt.tight_layout()

plt.show()

pos, neg = (top_pos_neg_words(yelp_freq))
plt.bar (list(neg.keys()), list(neg.values()), width = .3)
labels = (list(neg.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('Yelp Most Used Negative Words', loc='center')
plt.tight_layout()
plt.show()

pos, neg = (top_pos_neg_words(amazon_freq))
plt.bar (list(pos.keys()), list(pos.values()))
labels = (list(pos.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('Amazon Most Used Positive Words', loc='center')
plt.tight_layout()
plt.show()

pos, neg = (top_pos_neg_words(amazon_freq))
plt.bar (list(neg.keys()), list(neg.values()))
labels = (list(neg.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('Amazon Most Used Negative Words', loc='center')
plt.tight_layout()
plt.show()

pos, neg = (top_pos_neg_words(imdb_freq))
plt.bar (list(pos.keys()), list(pos.values()), width = .3)
# plt.setp(get_xticklabels(), rotation=30, horizontalalignment='right')
labels = (list(pos.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('IMDB Most Used Positive Words', loc='center')
plt.tight_layout()
plt.show()

pos, neg = (top_pos_neg_words(imdb_freq))
plt.bar (list(neg.keys()), list(neg.values()))
labels = (list(neg.keys()))
plt.xticks(labels, rotation='vertical')
plt.title('IMDB Most Used Negative Words', loc='center')
plt.tight_layout()
plt.show()


# Annoying is most used negative word in imdb, avoid in amazon, and bad in yelp domain. Amazing, awesome and amazing are most used positive words in yelp, amazon, imdb respectively. 
