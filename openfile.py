
fn = 'foods.txt'

def linetokey(line):
    key = line.split('/')[1]
    key = key.split(':')[0]
    return key
    
def getkeys():
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
    
def printlines(num=20):
    f = open(fn,'r')
    for i in range(num):
        print f.readline()
    return
    
   
printlines()   
print 'List of unique keys:', getkeys()