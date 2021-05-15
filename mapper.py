import sys
import re
import string

# text = open("name_of_file.txt" , "r", encoding="utf8")
# mapper = open("mapper.txt", 'w')

# reads from given txt file in the terminal
for line in sys.stdin:
    sent = line.strip()
    sent = sent.lower()
    sent = re.sub(f"[^{string.ascii_lowercase + ' '}]", '#', sent)
    sent = [sent[i:i + 2] for i in range(len(sent) - 1)]
    sent = map(lambda x: (x, 1), sent)
    print(list(sent))
    # mapper.write(str(list(sent))+"\n")