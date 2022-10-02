"""
nel caso in cui venga lanciato un errore sul certificato ssl eseguire i seguenti passaggi:
- installare certifi
- eseguire lo script install_certifi.py
"""

from email.message import EmailMessage
import ssl
import smtplib
import csv

sender_mail = "mail"
password = "password"

subject = "compilazione form yeswork - test"
body = """
Buongiorno, sono Alberto

Vi chiedo cortesemente il vostro aiuto nella compilazione del seguente questionario realizzato in collaborazione con la recente realtà di Yeswork, applicazione innovativa sviluppata da Il Lavoro in un Tocco s.r.l.

Yeswork è un’app che rivoluziona la ricerca del lavoro permettendo ad imprese, lavoratori e studenti di domandare e offrire prestazioni lavorative occasionali in momenti di necessità e senza vincolo contrattuale, retribuito e nel rispetto della legge. 
 
La vision di Yeswork è quella di “creare una Community di milioni di persone per migliorare la loro vita e quella degli altri, risolvendo problematiche quotidiane”. 
Al fine di realizzare un’accurata ricerca di mercato, vi chiedo gentilmente di dedicare 5 minuti alla compilazione del questionario che allego.

https://so7rs123rmm.typeform.com/to/QLy5Fixa

Vi ringrazio anticipatamente e vi porgo cordiali saluti.

"""


context = ssl.create_default_context()
with open("test-email.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for email in reader:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_mail, password)
            em = EmailMessage()
            em['From'] = sender_mail
            em['Subject'] = subject
            em.set_content(body)
            em['To'] = email
            smtp.sendmail(sender_mail, email, em.as_string())
            print(f"sent mail to {email}")
print("program finished")