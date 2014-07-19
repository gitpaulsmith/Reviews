import sys
import re
import json


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
    

def main():
    fn = 'foods.txt'
    printlines(fn)
    keylist = getkeys(fn)
    print 'List of unique keys:', keylist


if __name__ == '__main__':
    main()