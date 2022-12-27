import os.path

import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda x: x['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn_list = list()
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(str(vote[0].text).replace(' points', ''))
            if points > 199:
                href = fix_url(href)
                hn_list.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn_list)


def fix_url(url):
    if not str(url).startswith('http'):
        return f'{hn_url}{url}'
    return url


hn_url = 'https://news.ycombinator.com/'
mega_links = list()
mega_subtext = list()

qty_pages = 2
for i in range(1, qty_pages+1):
    res = requests.get(f'{hn_url}?p={i}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    mega_links += links
    mega_subtext += subtext

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
