from scraper import get_emails_from_url

# Input
websites: list = [
    "https://levius.it",
    "https://emiliodallatorre.it",
    "https://jeve.it"
]

# Processing
results: dict = {}
for website in websites:
    results[website] = get_emails_from_url(website)
print(results)

# Output
with open("results.csv", "w") as f:
    f.write("Website,Emails\n")
    for website, emails in results.items():
        for email in emails:
            f.write(f"{website},{email}\n")
