#import packages urllib & xml parsing
import xml.etree.ElementTree as ET 
import urllib.request, urllib.parse, urllib.error

url = input ("Enter location: ")
print ("Retrieving ", url)
data = urllib.request.urlopen(url).read()
print ("Retrieved ", len(data), "characters")
#print(data.decode())

count = 0
sum = 0
tree = ET.fromstring(data)
lst = tree.findall("comments/comment")

for item in lst:
     num = int(item.find("count").text)
     count = count + 1
     sum = sum + num
print ("Count: ", count)
print ("Sum: ", sum)
