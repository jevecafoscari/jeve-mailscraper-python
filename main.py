import csv
from scraper import get_emails_from_url

# Input


# open the file in read mode
filename = open('website.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)
websites: list = []
for col in file:
    websites.append(col['Website'])


# Processing
results: dict = {}
counter: int = 0
for website in websites:
    results[website] = get_emails_from_url(website)
    counter += len(results[website])
print(f"Found {counter} emails for {len(websites)} websites!")

# Output
with open("results.csv", "w") as f:
    f.write("Website,Emails\n")
    for website, emails in results.items():
        for email in emails:
            f.write(f"{website},{email}\n")
