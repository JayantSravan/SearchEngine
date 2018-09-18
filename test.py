import os.path
from os import path
from Helpers import Preprocessor, Query
import pickle
import time
directory = 'data'

if not(os.path.exists(directory)):
    '''
    Checking if there exists a data directory. If no data, program quits.
    '''
    print('Data unavailable. Get the data using parsern file in helpers folder. Quitting now.')
    quit()

preP = Preprocessor.Preprocessor()  # creating a preprocessor file which contains tf-idf vector


if os.path.exists(directory + '/preprocessed.pickle'):  # check if the previously pickled file exists
    '''
    We need to pickle the object. If pickle exists, no need to compute again
    '''
    print('Preprocessed object exists. Parsing it.')
    pickle_in = open(directory + "/preprocessed.pickle", "rb")
    preP = pickle.load(pickle_in)
    pickle_in.close()

else:  # if it doesnt exist generate it
    start = time.time()
    print('Generating tf-idf vectors in: ')
    i = 0
    for filename in os.listdir(directory):  # iterating through the data directory and retrieving everything
        if os.path.exists(directory + '/' + filename) and path.isdir(directory + '/' + filename):
            print(filename)
            if filename == 'preprocessed.pickle':
                continue
            for file in os.listdir(directory + '/' + filename):
                if os.path.exists(directory + '/' + filename + '/' + file):
                    preP.compute_TFIDF_values(directory + '/' + filename + '/' + file, i)
                    i = i+1
    preP.make_TF_IDF_vector(i)
    end = time.time()
    pickle_out = open(directory + "/preprocessed.pickle", "wb")
    pickle.dump(preP, pickle_out)
    print('Took ' + str(end-start) + ' seconds to generate tf-idf tags. Pickling it.')
    pickle_out.close()

while True:  # take queries continuously
    queryStr = input("What is the dialogue you are looking for? say 'quit' to exit:")

    if queryStr == 'quit':  # quit if query says 'quit'
        quit()

    qu = Query.Query(queryStr)

    qu.process_query()
    results = qu.compute_results(len(preP.TF_IDF_vector), preP.TF_IDF_vector)

    count = 10
    for i in results:  # print top 10 results
       if count>0:
           print("File - ", preP.fileNum_to_file[i[1]], "   score = ",i[0])
           count -= 1
