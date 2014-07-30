#Converts the foods.txt file into a .csv file with the delimiter '\t!\t'
#Takes two arguments, the first being the name of the input .txt file, and the second the desired name of the output file

import sys
import os
import re
import argparse


def linetokey(line):
  #    key = line.split('/')[1]
  #    key = key.split(':')[0]
  match = re.search(r'/([-a-zA-Z]+):', line)
  key = match.group(1)
  return key


def getkeys(fn):
    #find unique keys in data
    keylist = []
    f = open(fn,'rb')
  
    for line in f:
      try:
        key = linetokey(line)
        if key not in keylist:
          keylist.append(key)
      except:
        pass
    f.close()
    return keylist


def validate(line, keylist):
    #Simple check to see if string holds correct number of entries
    matches = re.findall(r'\t!\t', line)
    if len(matches)==len(keylist)-1:
        return True
    else:
#        print('read error')
        return False


def write_file(fn, fout, keylist):
    f = open(fn, 'rb')
    g = open(fout, 'w')
  
    #Creates index
    writestr = ''
    for key in keylist:
      #separate with crazy delimiter unlikely to appear in user-entered content
      writestr += key+'\t!\t'
    g.write(writestr[:-3] + '\n')

    #Writes data from file
    writestr = ''
    for line in f:
      match = re.search(r'[a-z]+/([a-zA-Z]+):\s(.+)', line)
      if match:
        if match.group(1) in keylist:
          #use same crazy delimiter
          writestr += match.group(2)+'\t!\t'
      else:
        writestr = writestr[:-3] + '\n'
        if validate(writestr, keylist):
          g.write(writestr)
        writestr = ''
  
    f.close()
    g.close()


def main():
    parser = argparse.ArgumentParser(description='Converts text file into a csv file with a special delimiter')
    parser.add_argument('text')
    parser.add_argument('csv')
    args = parser.parse_args()

    keylist = getkeys(args.text)
    write_file(args.text, args.csv, keylist)

if __name__ == '__main__':
    main()
