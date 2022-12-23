import requests

res = requests.get('http://eddypagan.com')
sc = res.status_code  # 200 means everything is ok
res.raise_for_status()  # raise an exception if something was wrong

file = open('eddypagan.html', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)


