from twitter_scraper import get_tweets
import markovify
from urlextract import URLExtract


def fetch():
    tweets = ""
    for each in get_tweets("realDonaldTrump", pages=25):
        tweets += "".join(each["text"]) + " "
        
    extractor = URLExtract()
    urls = extractor.find_urls(tweets)
    
    for link in urls:
        tweets = tweets.replace(link, "")
    return tweets