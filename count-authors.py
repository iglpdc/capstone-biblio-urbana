# Counts line in a file
import sys
import csv

filename = sys.argv[1]

def append_last_name_authors(author_list, last_names):
    '''Get last name from author list'''
    for author in author_list:
        last_name = author.split(',')[0].strip()
        last_names.append(last_name)

last_names = []
with open(filename, 'r') as raw:
    reader = csv.reader(raw)
    for line in reader:
        authors_list = line[3].split(';')
        append_last_name_authors(authors_list, last_names)
print last_names
