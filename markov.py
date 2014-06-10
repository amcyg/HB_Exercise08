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
        if count > 139:
            break
        else:
            count += len(word) + 1
            tweet_list.append(word)

    tweet_list[0] = string.capitalize(tweet_list[0])

    if tweet_list[-1][-1] != '.':
        tweet_list[-1] = tweet_list[-1] + '.'


    tweet_text = " ".join(tweet_list)

    return tweet_text

def make_chains(corpus, n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    markov_dict ={}

    text = corpus.read()
    text = text.rstrip()
    words = text.split()

    index = 0
    while index < ( len(words) - 2 ):
        word1 = words[index]
        word2 = words[index + 1]
        word3 = words[index + 2]

        key = (word1, word2)

        if key in markov_dict:
            markov_dict[key] = markov_dict[key] + [word3]
        else:
            markov_dict[key] = [word3]
        index += 1

    corpus.close()

    return markov_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    text_list = []

    # pick a random key to start with
    first = random.sample(chains.keys(), 1)
    first_word = first[0][0]
    second_word = first[0][1]

    text_list.append(first_word)
    text_list.append(second_word)

    # start looking up keys for subsequent text

    index = 0
    while True:
        word1 = text_list[index]
        word2 = text_list[index + 1]
        key = (word1, word2)
        if key in chains:
            word3 = random.choice(chains[key])
            text_list.append(word3)
            index += 1
        else:
            break

    #return " ".join(text_list)
    return text_list


def main():
    script, filename = sys.argv

    # Change this to read input_text from a file
    
    input_text = open(filename)

    #TODO: make chain_dict create n-grams.
    chain_dict = make_chains(input_text, n)
    
    #changing random_text to be a list.
    random_text = make_text(chain_dict)
    # print random_text

    tweet = twitterize(random_text)
    print tweet

    input_text.close()

if __name__ == "__main__":
    main()
