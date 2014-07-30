import csv
import sys

def removeNonAsciiString(s): 
    ''' Returns the string without non ASCII characters'''
    for words in s:
    	for c in words:
			stripped = (c for c in words if 0 < ord(c) < 127)    
    return ''.join(stripped)
	
def removeNonAscii(filename):
 	csv_filename = filename
 	print "Opening CSV file: ",csv_filename 
 	f=open(csv_filename, 'r')
 	new_csv_filename='corrected'+filename
 	g=open(new_csv_filename,'w')
 	writer = csv.writer(g)

 	tempreader=csv.reader(f)

 	for row in tempreader:
 		removeNonAsciiString(row)
 		writer.writerow(row)

 	print 'A corrected',filename,' file has been created.'
