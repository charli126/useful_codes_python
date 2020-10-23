import re
hand = open ("mbox-short.txt")
print (hand.read())

for line in hand:
    line = line.rstrip()
    fline = re.findall ("^From .*@([^ ]*)", line)
    #otherwise too many empty lines
    if len(fline) < 1:
        continue
    print (fline)
    #ad = re.findall ("@([^ ]*)", fline)
    #print (ad)
    #empty lists show up too
