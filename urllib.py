import urllib.request, urllib.parse, urllib.error
counts = dict()
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print (line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 

print (counts)
lst = list()
for k, v in counts.items():
    lst.append((v, k))

print (lst)
lst = sorted(lst)

for v, k in lst:
    print (k, v)
