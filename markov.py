#!/usr/bin/env python

import sys
import random
import string

def twitterize(text):
    """Takes randomly generated text and compresses it into a 
    140 characters (or less)"""

    tweet_list = []
    count = 0

    for word in text:
        word_length = len(word)
        if (count + word_length) > 139:
            break
        else:
            count += word_length + 1
            tweet_list.append(word)

    # capitalizes first word of tweet
    tweet_list[0] = string.capitalize(tweet_list[0])

    # adds period to end of tweet.
    if tweet_list[-1][-1] != '.':
        tweet_list[-1] = tweet_list[-1] + '.'


    tweet_text = " ".join(tweet_list)

    print "This tweet is %d characters long." % len(tweet_text)

    return tweet_text

def make_chains(corpus, n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    markov_dict ={}

    text = corpus.read()
    text = text.rstrip()
    words = text.split()

    index = 0
    while index < ( len(words) - n ):
        key_list = words[index:n + index]
        value = words[n + index]

        key = tuple(key_list)

        if key in markov_dict:
            markov_dict[key] = markov_dict[key] + [value]
        else:
            markov_dict[key] = [value]
        
        index += 1

    corpus.close()

    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    text_list = []

    # pick a random key to start with
    first = random.sample(chains.keys(), 1)

    first_words = first[0]

    text_list = text_list + list(first_words)

    # print text_list

    # start looking up keys for subsequent text

    n = len(first_words)
    index = 0
    while True:
        key_list = text_list[index:n + index]
        key = tuple(key_list)
        if key in chains:
            next_word = random.choice(chains[key])
            text_list.append(next_word)
            index += 1
        else:
            break

    return text_list


def main():
    #script, filename = sys.argv
    filename = "darwin.txt"


    #ngram = int(raw_input("How many n-grams? "))
    ngram = 2


    # Change this to read input_text from a file
    
    input_text = open(filename)


    chain_dict = make_chains(input_text, ngram)
    
    #changing random_text to be a list.
    random_text = make_text(chain_dict)
    # print random_text

    tweet = twitterize(random_text)
    return tweet

    input_text.close()

if __name__ == "__main__":
    main()
