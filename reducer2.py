import sys

en_score = 0
nl_score = 0

for line in sys.stdin:
    lang, point = line.split('\t', 1)

    if lang == 'en':
        en_score += 1
    else:
        nl_score += 1

print(f"Total found nl sentences: {nl_score}\nTotal found en sentences {en_score}")