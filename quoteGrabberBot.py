#! python3
# quoteGrabberBot.py - Scrapes quotes from goodreads.com
import requests
import os
import bs4

# Starting url
url = 'http://www.goodreads.com/quotes/tag/motivational'
raw_quotes = []

# Scrapes until we reach the 100th page
while not url.endswith('100'):
    print("=========================")
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Remove all script and style elements from HTML
    for script in soup(["script", "style"]):
        script.extract()

    quotes = soup.select('div.quoteText')

    for quote in quotes:
        splitQuote = quote.getText().split()
        cleanQuote = ' '.join(splitQuote)
        raw_quotes.append(cleanQuote + "\n")
        print(cleanQuote)

    nextLink = soup.select('a.next_page')
    url = 'http://www.goodreads.com' + nextLink[0].get('href')

# Filter out quotes that are not Twitter friendly (> 140 characters)
clean_quotes = open('quotes.txt', 'a')

print("Cleaning tweets ...")

# TODO: Parse quotes to check for english?
for quote in raw_quotes:
    if (len(quote) <= 140):
        clean_quotes.write(quote)
    else:
        print("Deleted: " + quote)

clean_quotes.close()

print('Done.')
