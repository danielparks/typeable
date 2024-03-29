# Counts the number of per-hand runs in a string
#
# aaaa - 3 runs
# apap - 0 runs
# aapa - 1 runs
def count(test_string, hands):
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

# Runs/(character count - 1)
def fraction(test_string, hands):
    if len(test_string) <= 1:
        fraction = 0
    else:
        runs = count(test_string, hands)
        fraction = runs/(len(test_string)-1)
    return fraction
