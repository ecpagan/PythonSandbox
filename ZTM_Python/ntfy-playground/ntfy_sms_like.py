import requests

my_topic = ''
message = 'Happy Holidays! 😀'
requests.post(f'https://ntfy.sh/{my_topic}',
              data=f'{message}'.encode(encoding='utf-8'))
print('Done')
