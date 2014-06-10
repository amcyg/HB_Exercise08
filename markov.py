#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    markov_dict ={}

    text = corpus.read()
    text = text.rstrip()
    text = string.replace(text, "\n", " ")
    words = text.split(" ")

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
            #print text_list
        else:
            break

    return " ".join(text_list)


def main():
    script, filename = sys.argv

    # Change this to read input_text from a file
    
    input_text = open(filename)

    chain_dict = make_chains(input_text)
    print chain_dict
    
    random_text = make_text(chain_dict)
    print random_text

    input_text.close()

if __name__ == "__main__":
    main()
