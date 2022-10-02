"""
nel caso in cui venga lanciato un errore sul certificato ssl eseguire i seguenti passaggi:
- installare certifi
- eseguire lo script install_certifi.py
"""

from email.message import EmailMessage
import ssl
import smtplib

from_address = "inserire la main"
password = "password per il commit"
to_address = "inserire il ricevente"

subject = "inserire l'oggetto della mail"
body = "inserire il corpo della mail"

em = EmailMessage()
em['From'] = from_address
em['To'] = to_address
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(from_address, password)
    smtp.sendmail(from_address, to_address, em.as_string())

print("program finished")