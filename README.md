# SearchEngine

This search engine can be used to find out which episode of your favorite TV series had a particular dialogue. It uses tf-idf model along with a n-gram model search.

# Requirements
nltk
pickle
urllib
beautifulsoup4

# Data 
The data folder in the root directory should contain the documents to be searched for. To generate the data, run the Scraper.py script from Helpers and populate the directory in the format - 'data/'TV Series name'/'Episode Name'.txt

# Helpers
Helpers contain the scripts for precprocessing data and the queries.
It also contains a scraper script

# Usage
test.py script should be run to get the tf-idf vector and preocess queries. Running it for the first time may take some time because it has to process the entire data. After the first use, pickles are created to make the further processing easy.
