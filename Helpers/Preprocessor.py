from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string, math
import re

class Preprocessor:
    def __init__(self):
        self.TFVectors = {}
        self.IDFVector = {}
        self.fileNum_to_file = {}
        self.fileLengths = {}
        self.wordAppearancesInFiles = {}
        self.distinctWords = []
        self.TF_IDF_vector = {}

    def extractText(self, fileDir):
        try:
            f = open(fileDir, "r")

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
        tokens = word_tokenize(str) #convert the string into a list of tokens based on ' ' delimiter and other methods used by nltk
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

    def compute_TFIDF_values(self, fileDir, fileNum):
        try:
            self.fileNum_to_file[fileNum] = fileDir #associating file to a file number

            data = self.extractText(fileDir) #getting text from file
            tokens = self.tokenize(data) #tokenizing
            tokens = self.lemmatize(tokens) #lemmatizing

            self.fileLengths = len(tokens) #storing file lengths

            fileWordsCount = {} #to store the count of each word in this file

            for token in tokens: #increment the count of the token
                if token not in fileWords:
                    fileWordsCount[token] = 1
                else:
                    fileWordsCount[token] += 1

            self.TFVectors[fileNum] = fileWordsCount #associating the word counts of this file to the file number

            setOfWordsInFile = list(set(tokens)) #getting a list of distinct words using set function

            for word in setOfWordsInFile: #incrementing document frequency
                if word not in self.IDFVector:
                    self.distinctWords.append(word)
                    IDFVector[word] = 1
                else:
                    IDFVector[word] += 1

            for word in setOfWordsInFile: #storing the document numbers of the files where the word appeared
                if word not in self.wordAppearancesInFiles:
                    self.wordAppearancesInFiles[word] = [fileNum]
                else:
                    self.wordAppearancesInFiles[word].append(fileNum)

        except:
            print('issue in computing TF and IDF values', fileNum, ' - ', fileDir)

    def make_TF_IDF_vector(self, numOfFiles): #TF_IDF vector would be of the form [word][fileNum].
        for word in self.distinctWords: #iterate over all the words in the entire dataset
            term_TF_IDF = {}
            for fileNum in self.wordAppearancesinFiles[word]: #iterate over those files in whom this word is present
                try:
                    term_TF_IDF[fileNum] = (1+math.log10(self.TFVectors[fileNum][word]))*(math.log10(numOfFiles/IDFVector[word]))
                except:
                    print('Problem while making the TF_IDF vector')
            self.TF_IDF_vector[word] = term_TF_IDF
        return self.TF_IDF_vector

#just a demo script. Remove before the final release
p = Preprocessor()
print(p.stem(p.tokenize('Hey, this is a trial string. Let us see what happens')))
