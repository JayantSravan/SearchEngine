from Helpers.Preprocessor import Preprocessor

class Query:
<<<<<<< HEAD
    """
    A query class has methods required to handle a query. It uses the preprocessor class
    """
=======
    '''
    A query class has methods required to handle a query. It uses the preprocessor class
    '''
>>>>>>> eee7e39e2c0f24970eb4d6a76a00983d028e4259
    def __init__(self, str):
        self.preprocessor = Preprocessor() #to process the query to tokens
        self.all_words = [] #all words in the query (lemmatized)
        self.results = [] #list of docs and its scores
        self.query = str #query string

    def process_query(self):
<<<<<<< HEAD
        """
        Tokenize, lemmatize and get n-grams for a query
        :return:
        """
=======
        '''
        Tokenize, lemmatize and get n-grams for a query
        :return:
        '''
>>>>>>> eee7e39e2c0f24970eb4d6a76a00983d028e4259
        tokens = self.preprocessor.tokenize(self.query) #tokenize
        tokens = self.preprocessor.lemmatize(tokens) #lemmatize
        self.all_words = self.preprocessor.get_n_grams(tokens) #get n grams

    def compute_results(self, numOfFiles, TF_IDF_vector):
<<<<<<< HEAD
        """
=======
        '''
>>>>>>> eee7e39e2c0f24970eb4d6a76a00983d028e4259
        Compute the top matches for a particular query
        :param numOfFiles: total number of files in data
        :param TF_IDF_vector: tf-idf vector after n-gram model
        :return: the sorted list of matches
<<<<<<< HEAD
        """
=======
        '''
>>>>>>> eee7e39e2c0f24970eb4d6a76a00983d028e4259
        self.results = []
        for file_iter in range(numOfFiles):
            rating = 0.0
            for word in self.all_words:
                if word in TF_IDF_vector and file_iter in TF_IDF_vector[word]:
                    rating +=TF_IDF_vector[word][file_iter] #adding the TF-IDF values for common words from the vector
            self.results.append( (rating, file_iter) ) #tuple
        self.results = sorted(self.results, reverse = True) #sort tuple

        return self.results
