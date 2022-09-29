import csv
from scraper import Scraper

# Input
file_plaintext = open('website.csv', 'r')
file_csv = csv.DictReader(file_plaintext)
websites: list = []
for col in file_csv:
    websites.append(col['Website'])


# Processing
results: dict = {}
counter: int = 0

thread_pool: list = []

for website in websites:
    threaded_scraper: Scraper = Scraper(website)
    threaded_scraper.start()
    thread_pool.append(threaded_scraper)

for thread in thread_pool:
    results[thread.original_url] = thread.join()
    counter += len(thread.found_emails)

print(f"Found {counter} emails for {len(websites)} websites!")

# Output
with open("results.csv", "w") as f:
    f.write("Website,Emails\n")
    for website, emails in results.items():
        for email in emails:
            f.write(f"{website},{email}\n")
