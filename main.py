import csv
from scraper import Scraper
from tqdm import tqdm

# Input
file_plaintext = open('website.csv', 'r')
file_csv = csv.DictReader(file_plaintext)
websites: list = []
for col in file_csv:
    websites.append(col['Website'])
i = 0
while i < len(websites):
    #print(websites[i])
    if websites[i].find('http://') == -1:
        #print('... fix ... ')
        temp = websites[i]
        websites[i] = 'http://' + temp
        #print(websites[i])
    i += 1


# Processing
results: dict = {}
counter: int = 0
thread_pool: list = []

print("Booting up web scrapers...")
for i in tqdm(range(len(websites))):
    threaded_scraper: Scraper = Scraper(websites[i])
    threaded_scraper.start()
    thread_pool.append(threaded_scraper)

print("\nWaiting for threads to finish...")
for i in tqdm(range(len(thread_pool))):
    results[thread_pool[i].original_url] = thread_pool[i].join()
    counter += len(results[thread_pool[i].original_url])

print(f"Found {counter} emails for {len(websites)} websites!")


# Output
print("\nSaving results...")
with open("results.csv", "w") as f:
    f.write("Website,Emails\n")

    websites: list = list(results.keys())
    for i in tqdm(range(len(websites))):
        website = websites[i]
        emails = results[website]
        for email in emails:
            f.write(f"{website},{email}\n")

print("\nDone!")
