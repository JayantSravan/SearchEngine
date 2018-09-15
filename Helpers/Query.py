from Helpers.Preprocessor import Preprocessor

class Query:
    def __init__(self, str):
        self.preprocessor = Preprocessor() #to process the query to tokens
        self.all_words = [] #all words in the query (lemmatized)
        self.results = [] #list of docs and its scores
        self.query = str #query string

    def process_query(self):
        tokens = self.preprocessor.tokenize(self.query) #tokenize
        self.all_words = self.preprocessor.lemmatize(tokens) #lemmatize


    def compute_results(self, numOfFiles, TF_IDF_vector):
        self.results = []
        for file_iter in range(numOfFiles):
            rating = 0.0
            for word in self.all_words:
                if word in TF_IDF_vector and file_iter in TF_IDF_vector[word]:
                    rating +=TF_IDF_vector[word][file_iter] #adding the TF-IDF values for common words from the vector
            self.results.append( (rating, file_iter) ) #tuple

        self.results = sorted(self.results, reverse = True) #sort tuple

        return self.results
