import sys
import re
#import sqlite3
import json
import pandas


def linetokey(line):
#    key = line.split('/')[1]
#    key = key.split(':')[0]
    match = re.search(r'/([-a-zA-Z]+):', line)
    key = match.group(1)
    return key


def getkeys(fn):
    #find unique keys in data
    keylist = []
    f = open(fn,'r')
    
    for line in f:
        try:
            key = linetokey(line)
            if key not in keylist:
                keylist.append(key)
        except:
            pass
    f.close()
    return keylist


def printlines(fn, num=20):
    f = open(fn,'r')
    for i in range(num):
        print f.readline()
    return


def write_file(fn, fout, keylist):
    f = open(fn, 'r')
    g = open(fout, 'w')
    
    writestr = ''
    for key in keylist:
        #separate with crazy delimiter unlikely to appear in user-entered content
        writestr += key+'\t!\t'
    g.write(writestr[:-3] + '\n')

    writestr = ''
    for line in f:
         match = re.search(r'[a-z]+/([a-zA-Z]+):\s(.+)', line)
         if match:
             if match.group(1) in keylist:
                 #use same crazy delimiter
                 writestr += match.group(2)+'\t!\t'
         else:
             g.write(writestr[:-3] + '\n')
             writestr = ''

    f.close()
    g.close()


def main():
    fn = 'foods.txt'
    fout = 'foods.csv'
    
#    in case we want to load data into a SQL database before a PANDAS data frame:
#
#    fdb = sqlite3.connect('foods.db')
#    c = fdb.cursor()
#    fdb.commit()
#    fdb.close()

#    printlines(fn)
    keylist = getkeys(fn)
#    print 'List of unique keys:', keylist
    write_file(fn, fout, keylist)
    df = pandas.io.parsers.read_table(fout, '\t!\t')
#    print df[:10]

if __name__ == '__main__':
    main()
