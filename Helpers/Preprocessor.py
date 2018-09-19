from nltk import word_tokenize, ngrams
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import string, math

class Preprocessor:
    """
    Preprocessor provides with necessary tools like text extraction,tokenization, stemming, lemmatization, tf-idf extraction,etc
    It stores the final tf-idf vector
    """
    def __init__(self):
        """
        Initializing variables to be used later
        """
        self.TFVectors = {}
        self.IDFVector = {}
        self.fileNum_to_file = {}
        self.fileLengths = {}
        self.wordAppearancesInFiles = {}
        self.distinctWords = []
        self.TF_IDF_vector = {}

    def extractText(self, fileDir):
        """
        Read a file and convert the content into a string
        :param fileDir: file's path
        :return: a string containing the content
        """
        try:
            f = open(fileDir, "r")

            txt = f.read()
            f.close()
        except:
            txt = "Something wrong in extracting text"
            print(txt)
        return txt

    def tokenize(self, str):
        """
        Uses nltk to tokenize a string
        :param str: string to be tokenized
        :return: a list of tokens
        """
        tokens = word_tokenize(str) #convert the string into a list of tokens based on ' ' delimiter and other methods used by nltk
        tokens = [i for i in tokens if i not in string.punctuation] #remove all the tokens which belong to punctuation
        tokens = [i for i in tokens if len(i)>1] #remove all the words whose length is not more than 1
        return tokens

    def stem(self, tokens):
        """
        Uses nltk to stem tokens
        :param tokens: list of strings to be stemmed
        :return: a list of stemmed tokens
        """
        stemmedWords = [] #defined an empty list to append the stemmed tokens
        stemmerMechanism = PorterStemmer() #get a porter stemmer
        for i in tokens:
            stemmedWords.append(stemmerMechanism.stem(i)) #append stemmed tokens to the list
        return stemmedWords

    def get_n_grams(self, tokens):
        """
        Gets n_grams upto size 2
        :param tokens: tokens to which n grams have to be generated
        :return: a list of n-grams
        """
        unigram = [' '.join(word) for word in ngrams(tokens,1)]
        bigram = [' '.join(word) for word in ngrams(tokens,2)]
        return unigram + bigram

    def lemmatize(self, tokens):
        """
        Use lemmatizer or the stemmer, not both. Using this would be preferred for better results.
        :param tokens: A list of tokens to be lemmatized
        :return: lemmatized tokens
        """
        lemmatizedWords = [] #defined an empty list to append the lemmatized tokens
        lemmatizer = WordNetLemmatizer() #get a Word Net Lemmatizer
        for i in tokens:
            lemmatizedWords.append(lemmatizer.lemmatize(i)) #append lemmatized tokens to the list
        return lemmatizedWords

    def compute_TFIDF_values(self, fileDir, fileNum):
        """
        Computing tf-idf values for a file
        :param fileDir: path of the file
        :param fileNum: file num of the file
        :return:
        """
        try:
            self.fileNum_to_file[fileNum] = fileDir #associating file to a file number

            data = self.extractText(fileDir) #getting text from file
            tokens = self.tokenize(data) #tokenizing
            tokens = self.lemmatize(tokens) #lemmatizing
            tokens = self.get_n_grams(tokens) #get n grams


            self.fileLengths = len(tokens) #storing file lengths

            fileWordsCount = {} #to store the count of each word in this file

            for token in tokens: #increment the count of the token
                if token not in fileWordsCount:
                    fileWordsCount[token] = 1
                else:
                    fileWordsCount[token] = fileWordsCount[token] + 1

            self.TFVectors[fileNum] = fileWordsCount #associating the word counts of this file to the file number

            setOfWordsInFile = list(set(tokens)) #getting a list of distinct words using set function
            for word in setOfWordsInFile: #incrementing document frequency
                if word not in self.IDFVector:
                    self.distinctWords.append(word)
                    self.IDFVector[word] = 1
                else:
                    self.IDFVector[word] += 1
            for word in setOfWordsInFile: #storing the document numbers of the files where the word appeared
                if word not in self.wordAppearancesInFiles:
                    self.wordAppearancesInFiles[word] = [fileNum]
                else:
                    self.wordAppearancesInFiles[word].append(fileNum)
        except:
            print('issue in computing TF and IDF values', fileNum, ' - ', fileDir)

    def make_TF_IDF_vector(self, numOfFiles):
        """
        Get a vector tf-idf for all the files
        TF_IDF vector would be of the form [word][fileNum] dictionary.
        :param numOfFiles: total number of files
        :return: a tf-idf vector
        """
        for word in self.distinctWords: #iterate over all the words in the entire dataset
            term_TF_IDF = {}
            for fileNum in self.wordAppearancesInFiles[word]: #iterate over those files in whom this word is present
                try:
                    term_TF_IDF[fileNum] = (1.0 + math.log10(self.TFVectors[fileNum][word])) * (math.log10(numOfFiles/self.IDFVector[word]))
                except:
                    print('Problem while making the TF_IDF vector')
            self.TF_IDF_vector[word] = term_TF_IDF
        return self.TF_IDF_vector

#just a demo script. Remove before the final release
#p = Preprocessor()
#print(p.get_n_grams(p.stem(p.tokenize('Hey, this is a trial string. Let us see what happens'))))
