import requests as rq

url = 'https://news.google.com/rss/search?q=accenture&hl=en-IN&gl=IN&ceid=IN:en'

data= rq.get(url)
print(data.text)