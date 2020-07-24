import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Alex Costan'
email['to'] = 'acostan@fau.edu'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('alexcostan13@gmail.com', 'wouldntyouliketoknow:)')
    smtp.send_message(email)
    print('all good boss!')
