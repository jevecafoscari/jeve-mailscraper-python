import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
from threading import Thread


class Scraper(Thread):
    original_url: str
    found_emails: set

    def __init__(self, original_url):
        self.original_url = original_url
        Thread.__init__(self)

    def run(self):
        print(f"Avviato {self.original_url}")

        unscraped = deque([self.original_url])  
        scraped = set()  
        emails = set()  

        while len(unscraped):
            # Find the correct usable URL
            url = unscraped.popleft()  
            scraped.add(url)
            parts = urlsplit(url)

            base_url = "{0.scheme}://{0.netloc}".format(parts)
            if '/' in parts.path:
                path = url[:url.rfind('/')+1]
            else:
                path = url
            # print(f"Scraping URL: {url}")

            # Get the HTML
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            # Extract all email addresses and add them into the resulting set
            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z\.\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails) 

            soup = BeautifulSoup(response.text, 'lxml')

            for anchor in soup.find_all("a"):
                if "href" in anchor.attrs:
                    link = anchor.attrs["href"]
                else:
                    link = ''

                    if link.startswith('/'):
                        link = base_url + link
                    
                    elif not link.startswith('http'):
                        link = path + link

                    if not link in unscraped and not link in scraped:
                            unscraped.append(link)

        self.found_emails = emails

    def join(self, timeout=None):
        Thread.join(self, timeout=timeout)
        print(f"Completato {self.original_url}")
        return self.found_emails
