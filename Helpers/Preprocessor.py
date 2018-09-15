from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string, math
import re

class Preprocessor:
    def __init__(self):
        pass

    def extractText(self, filename):
        try:
            f = open(filename, "r")

            txt = f.read()
            txt = txt.decode('utf-8')
            txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
            txt = txt.encode('ascii','ignore') #removes unicode characters like \u0097 and type(txt) is bytes
            txt = txt.split()
            temp = []
            for text in txt:
                try:
                    temp.append(text.decode('unicode_escape')) # conversion to desired string
                except:
                    pass
                txt = ' '.join(newTxt)
            f.close()
        except:
            txt = "Something wrong in extracting text"
            print(txt)
        return txt

    def tokenize(self, str):
        tokens = word_tokenize(str) #convert the string into a list of tokens based on ' ' delimiter
        tokens = [i for i in tokens if i not in string.punctuation] #remove all the tokens which belong to punctuation
        tokens = [i for i in tokens if len(i)>1] #remove all the words whose length is not more than 1
        return tokens

    def stem(self, tokens):
        stemmedWords = [] #defined an empty list to append the stemmed tokens
        stemmerMechanism = PorterStemmer() #get a porter stemmer
        for i in tokens:
            stemmedWords.append(stemmerMechanism.stem(i)) #append stemmed tokens to the list
        return stemmedWords

    def lemmatize(self, tokens): #use lemmatizer or the stemmer, not both. Using this would be preferred for better results
        lemmatizedWords = [] #defined an empty list to append the lemmatized tokens
        lemmatizer = WordNetLemmatizer() #get a Word Net Lemmatizer
        for i in tokens:
            lemmatizedWords.append(lemmatizer.lemmatize(i)) #append lemmatized tokens to the list
        return lemmatizedWords

    
#just a demo script. Remove before the final release
p = Preprocessor()
print(p.stem(p.tokenize('Hey, this is a trial string. Let us see what happens')))
