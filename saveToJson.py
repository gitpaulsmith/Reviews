from JsonSave import *
from correctCSV import removeNonAscii
import csv
import pandas as pd

def main():
	convertToJson('foods.csv')
	f=open('foods.json','r')
	df=pd.io.json.read_json(f)
	print df.shape

if __name__ == '__main__':
    main()