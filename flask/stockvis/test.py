from csv import DictReader
import requests
from StringIO import StringIO

site = "http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=2013"
f = StringIO(requests.get(site).content)


fn = ("Date", "Open", "High", "Low", "Close", "Volume", "Adj")
reader = DictReader(f, fn)
print([r for r in reader])
