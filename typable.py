#!/usr/bin/env python3

import sys

qwerty = [
    "`~12345~!@#$%123456qwertasdfgzxcvb\t",
    "67890-=^&*()_+yuiop[]\\{}|hjkl;':\"nm,./<>?"]
qwerty = [set(chars.lower() + chars.upper()) for chars in qwerty]

test_string = sys.argv[1]
print("String to test:", repr(test_string))

counts = [0 for _ in qwerty]
for c in test_string:
    for index, chars in enumerate(qwerty):
        if c in chars:
            counts[index] += 1

min_count = min(counts)
max_count = max(counts)
for count in counts:
    print("hand: {:3.0f}% ({})".format(count/len(test_string)*100, count))

print()
print("SCORE: {:.0f}%".format(100 - 100*(max_count-min_count)/len(test_string)))
