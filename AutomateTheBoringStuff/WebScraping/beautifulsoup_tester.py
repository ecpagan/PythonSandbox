import bs4
import requests

res = requests.get('http://eddypagan.com')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elem = soup.select('#antonio-barnett > strong')
name = elem[0].text.strip()
