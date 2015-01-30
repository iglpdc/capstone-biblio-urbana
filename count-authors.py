'''Counts how many times someone has authored a paper

Usage: count-authors.py <biblio.csv>
Parameters:
    biblio.csv: a csv file with bibliograpy
'''
import sys
import csv

filename = sys.argv[1]

def append_last_name_authors(author_list, last_names):
    '''Append author's last name to a list'''
    for author in author_list:
        last_name = author.split(',')[0].strip()
        last_names.append(last_name)

def count_items(items):
    '''Counts the number of times each item appears in a list'''
    result = {}
    for item in items:
        if item in result.keys():
            result[item] += 1
        else:
            result[item] = 1
    return result

last_names = []
with open(filename, 'r') as raw:
    reader = csv.reader(raw)
    for line in reader:
        authors_list = line[3].split(';')
        append_last_name_authors(authors_list, last_names)

author_counts = count_items(last_names)
max_times_authored = max(author_counts.values())
print max_times_authored
print author_counts
