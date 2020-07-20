from nltk.corpus import brown
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from string import punctuation
from rake_nltk import Rake
import json
import nltk

nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

with open("en.json") as json_data:
    en_json = json.load(json_data)

stopwords_json_en = set(en_json)
stopwords_nltk_en = set(stopwords.words('english'))
stopwords_punct = set(punctuation)
# Combine the stopwords.
stoplist_combined = set.union(stopwords_json_en, stopwords_nltk_en, stopwords_punct)

porter = PorterStemmer()
wnl = WordNetLemmatizer()

def penn2morphy(penntag):
    """ Converts Penn Treebank tags to WordNet. """
    morphy_tag = {'NN':'n', 'JJ':'a',
                  'VB':'v', 'RB':'r'}
    try:
        return morphy_tag[penntag[:2]]
    except:
        return 'n'

def lemmatize_sent(text):
    # Text input is string, returns lowercased strings.
    return [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
            for word, tag in pos_tag(word_tokenize(text))]

def lemmatize_sent_with_rake(text):
    rake = Rake(stopwords=set.union(stopwords_json_en, stopwords_nltk_en),
                punctuations = stopwords_punct,language = 'English')
    rake.extract_keywords_from_text(text)
    key_words = rake.get_ranked_phrases()
    # pos_tag(key_words)
    return [wnl.lemmatize(word.lower(), pos=penn2morphy(tag))
            for word, tag in pos_tag(key_words)]

def to_count_vec(string):
    analysis = [word for word in lemmatize_sent(string)
       if word not in stoplist_combined
       and not word.isdigit() ]
    return analysis

def to_count_vec_with_rake(string):
    analysis = [word for word in lemmatize_sent_with_rake(string)
       if word not in stoplist_combined
       and not word.isdigit() ]
    return analysis