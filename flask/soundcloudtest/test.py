import csv
import json
import requests

site = "http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=2014"
a = requests.get(site).content
a = a[:152]
a = a[:35]+a[41:]
print(a)

out = open("asdf.txt", "w+")
out.write(a)
out.close()

fn = ("Date", "Open", "High", "Low", "Close", "Volume", "Adj")
reader = csv.DictReader(open("asdf.txt"))

for row in reader:
    print(type(row))
    print(row)
