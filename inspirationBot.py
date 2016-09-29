#! python3
# inspirationBot.py - Takes input from quotes.txt, tweets quote + hashtag
# every 30 minutes

import tweepy
import time
import sys
from datetime import datetime
from random import randint

# Credentials to access Twitter API
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Initialize inspirationBot access to API + file input
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
inspirationBot = tweepy.API(auth)
quotes_file = open('quotes.txt', 'r')
quotes_list = []
hashtags = ["#inspiration", "#inspire",
            "#motivation", "#positivity", "#believe"]

# Parse quotes_file
print("Parsing quotes.txt...")
for line in quotes_file:
    quote = line.strip('\n')
    quotes_list.append(quote)
quotes_file.close()

for q in quotes_list:
    try:
        # Generate random hashtag
        hashtag = hashtags[randint(0, len(hashtags) - 1)]

        # Check if length of quote + " " + hashtag is valid tweet length
        if ((len(q) + len(hashtag) + 1) <= 140):
            tweet = q + " " + hashtag
        else:
            tweet = q

        # Send to Twitter & log tweet
        inspirationBot.update_status(tweet)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " -- " + tweet)
        quotes_list.remove(q)

        # Tweet every 30 minutes
        time.sleep(1800)

    # Ends execution on CTRL-C
    except KeyboardInterrupt:
        break

# Saves the remaining quotes to a txt file
quotes_file = open('quotes.txt', 'w')
print("\nRewriting quotes to quotes.txt...")
for q in quotes_list:
    quotes_file.write(q + "\n")
quotes_file.close()
