import os
from Helpers import Preprocessor,Query
directory = 'data'

preP = Preprocessor.Preprocessor()

i = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filename = directory + '/' + filename
        preP.compute_TFIDF_values(filename, i)
        i = i+1
preP.make_TF_IDF_vector(i)

#qu = Query.Query('Study Furthermore Teaching goal passion nanna leadership students enjoy')
qu = Query.Query('influences word choices, students')

qu.process_query()
results = qu.compute_results(i, preP.TF_IDF_vector)

for i in results:
    print("File - " , preP.fileNum_to_file[i[1]], "   score = " ,i[0])
#print(results)
