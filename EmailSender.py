import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # use instead of os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Alex Costan'
email['to'] = 'acostan@fau.edu'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('alexcostan13@gmail.com', 'wouldnt you like to know :)')
    smtp.send_message(email)
    print('all good boss!')
