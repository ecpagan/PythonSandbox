import smtplib

from_email = 'ecpagan+github@gmail.com'
to_email = from_email
body = 'Subject: Test1\n\nDear ecpagan, ...\n\n'

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()  # to start the connection
conn.starttls()
conn.login(from_email, '<password>')
conn.sendmail(from_email, to_email, body)
conn.quit()
