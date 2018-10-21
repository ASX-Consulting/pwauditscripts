#!/usr/bin/python3
# Pulls basic info and stats from haveibeenpwned
import json
import requests

printData = False

r = requests.get('https://haveibeenpwned.com/api/v2/breaches')
if r.status_code == 200:
    j = json.loads(r.text)
else:
    print('HTTP Status Code: ' + str(r.status_code))
    exit(5)
count = 0
total = 0
for record in j:
    print(record["Name"] + ", ", end="")
    print(record["BreachDate"] + ", ", end="")
    print(str(record["PwnCount"]),end="")
    if printData == True: 
        print(" [", end="")
        for data in record["DataClasses"]: 
            print(data, end="")
        print ("]",)
    else:
        print()
    count += 1
    total = total + record["PwnCount"]
print("Total number of breaches..............: " + str(count))
print("Total number of pwn'ed records........: ", end="")
print("{:,}".format(total))
