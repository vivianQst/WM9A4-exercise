"""
Word Filter and Counter Function

Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted.
2. filter_words (list of strings): A list of words to be filtered out from the text.

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""

import re

def word_filter_counter(text, filter_words):
    # Convert the text to lowercase to make the comparison case-insensitive
    text_lower = text.lower()

    # Split the text into words using regular expressions
    words = re.findall(r'\b\w+\b', text_lower)

    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Count the occurrences of filtered words
    for word in filter_words:
        word_counts[word] = words.count(word.lower())

    return word_counts
    


# Test cases
print(word_filter_counter("Hello world, hello!", ["hello"]))  # Expected output: {'hello': 2}
print(word_filter_counter("The quick brown fox.", ["the"]))  # Expected output: {'the': 1}
print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]))  # Expected output: {'we': 1, 'the': 1, 'or': 1}
