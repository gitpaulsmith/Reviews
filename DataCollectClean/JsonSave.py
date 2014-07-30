import json
import csv
import sys
from correctCSV import removeNonAscii

fieldnames=["productId","userId","profileName","helpfulness","score","time", "summary", "text"]

def convertToJson(filename):
	
	removeNonAscii(filename)
 	corrected_filename = 'corrected'+filename

	print "Opening CSV file: ",corrected_filename
 	f=open(corrected_filename, 'r')
 	csv_reader = csv.DictReader(f,fieldnames)

	json_filename = filename.split(".")[0]+".json"
 	print "Saving JSON to file: ",json_filename
 	jsonf = open(json_filename,'w') 
 	data = json.dumps([r for r in csv_reader],encoding='latin1')
 	jsonf.write(data) 
 	f.close()
 	jsonf.close()
