"""This file will execute our Markov chain project."""

import markovify
from fetch_data import fetch

def main():
    tweets = fetch()
    text = markovify.Text(tweets)
    print(text.make_short_sentence(max_chars=240, min_chars=60, tried=50))
    
if __name__ == "__main__":
    main()