import csv
from scraper import get_emails_from_url

# Input
file_plaintext = open('website.csv', 'r')
file_csv = csv.DictReader(file_plaintext)
websites: list = []
for col in file_csv:
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
