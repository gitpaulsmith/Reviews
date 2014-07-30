import sys
import os
import string
import argparse

#Similar to correctCSV.py

def simple_scrub(fin, fout):
  f = open(fin, 'rb')
  g = open(fout, 'wb')

  for line in f:
    filter(lambda x: x in string.printable, line)
    g.write(line)
  f.close()
  g.close()


def main():
  parser = argparse.ArgumentParser(description='Scrubs a .csv file of non-ASCII characters')
  parser.add_argument('csvin')
  parser.add_argument('csvout')
  args = parser.parse_args()
  
  simple_scrub(args.csvin, args.csvout)

if __name__ == '__main__':
  main()
