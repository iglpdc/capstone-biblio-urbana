# Counts line in a file
import sys
filename = sys.argv[1]

count = 0
with open(filename, 'r') as reader:
    for line in reader:
        count += 1

print count
