# Waleed Yusuf
# 2104654

import csv

filename = input()
words = []
new_words = []
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        for word in row:
            words.append(word)
        for word in words:
            freq = words.count(word)
            if word not in new_words:
                new_words.append(word)
                print(word, freq)
