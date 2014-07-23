Reviews
=======

The script openfile.py was the initial attempt for converting the text file from Amazon into a csv file that could then be read into a dataframe. This is also the purpose of txt_to_csv.py, which was split off to include a bit of command-line optionality plus an elementary data validation function that excludes data with missing or incorrectly ordered fields.

The family of files correctCSV.py, JsonSave.py, and saveToJson.py all go together. The purpose of correctCSV.py is to remove non-ASCII characters from an existing CSV file. It appears that at present this script adds spurious quotation marks to the output file. The file scrub.py is a command-line implementation that preserves only printable characters. The purpose of JsonSave.py is to convert the corrected CSV file into a JSON file. The script saveToJson.py is a command line script that runs the CSV-to-JSON conversion and loads the JSON file as a pandas dataframe.

SimpleHist.ipynb and its extension SimpleHistExt.ipynb include some of our initial data analysis. Some work on sentiment analysis is found in nltk_notebook.ipynb and TwoSents.ipynb (TextBlob supports two different types of sentiment analysis). The .pickle file supports nltk_notebook.ipynb. TwoSents.ipynb has been deleted, as we will no longer be using TextBlob.

A Naive Bayes approach to classification is found in Scikit_NB.ipynb.

An SVM approach to classification is found in LinearSVM.ipynb.

ScrapeAmazon.py.ipynb obtains product names for given product IDs and top100titles.pkl was obtained from Amazon using the scraper.