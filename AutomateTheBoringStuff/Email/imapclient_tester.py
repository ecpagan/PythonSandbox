# import imaplib  # this is the one that comes with python, but is really hard to use, will use third party instead
import imapclient
import pyzmail


conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('ecpagan+github@gmail.com', '<password>')
conn.select_folder('INBOX', readonly=True)
# uids = conn.search()
uids = conn.gmail_search('after:2022/8/26')

raw_message = conn.fetch(uids[0], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(raw_message[uids[0]][b'BODY[]'])
subject = message.get_subject()
from_address = message.get_address('from')
to_address = message.get_address('to')
bcc_address = message.get_address('bcc')
text_part = message.text_part
html_part = message.html_part
charset = message.text_part.charset
if charset is None:
    charset = 'utf-8'
get_payload = message.text_part.get_payload().decode(charset)

folders_list = conn.list_folders()
