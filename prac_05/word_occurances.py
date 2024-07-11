"""
CP1404 Practical 5 - Word Occurrences
Sam Butters

Estimate: 25 minutes
Actual: 26:33
"""

from operator import itemgetter

word_to_count = {}

word_string = input("Enter a string: ")
words = word_string.split(" ")
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_word_length = max(len(word) for word in word_to_count)
sorted_word_to_count = sorted(word_to_count.items(), key=itemgetter(1), reverse=True)

for word, count in sorted_word_to_count:
    print(f"{word:{max_word_length}} : {count}")
