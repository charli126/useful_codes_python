name = input ("Enter file name: ")
try: 
    ofile = open (name)
except: 
    print ("file not found: ", name)
    quit()
emails = list()
count = 0
for line in ofile:
    line = line.rstrip()
    if len(line) < 3 or not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    emails.append(email)
    count = count + 1

for email in emails:
    print (email)

print ("There were", count, 
"lines in the file with From as the first word")
