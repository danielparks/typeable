#!/usr/bin/env python3

import sys

qwerty = [
    "`~12345~!@#$%123456qwertasdfgzxcvb\t",
    "67890-=^&*()_+yuiop[]\\{}|hjkl;':\"nm,./<>?"]
qwerty = [set(chars.lower() + chars.upper()) for chars in qwerty]

test_string = sys.argv[1]
print("String to test:", repr(test_string))

def count_runs(test_string, hands):
    runs = 0
    last_group = None
    for c in test_string:
        for group, chars in enumerate(hands):
            if c in chars:
                if last_group == group:
                    runs += 1
                last_group = group
                break
        else:
            last_group = None
    return runs

runs = count_runs(test_string, qwerty)
if runs == 0:
    percent = 0
else:
    percent = runs/(len(test_string)-1)

print("runs: {:.0f}%".format(percent*100))
