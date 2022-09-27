from scraper import get_emails_from_url

# Input
# TODO: Implement reading websites list from CSV / Excel.
websites: list = [
    "https://levius.it",
    "https://emiliodallatorre.it",
    "https://jeve.it"
]

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
