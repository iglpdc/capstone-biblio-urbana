'''Counts how many times someone has authored a paper

Usage: count-authors.py <biblio.csv>
Parameters:
    biblio.csv: a csv file with bibliograpy
'''
import sys
import csv

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

def find_keys_for_value(dictionary, desired_value):
    '''Finds the key corresponding to a given value in a dict'''
    result = []
    for key, value in dictionary.iteritems():
        if value == desired_value:
            result.append(key)
    return result

filename = sys.argv[1]

last_names = []

with open(filename, 'r') as raw:
    reader = csv.reader(raw)
    for line in reader:
        authors_list = line[3].split(';')
        append_last_name_authors(authors_list, last_names)

author_counts = count_items(last_names)
max_times_authored = max(author_counts.values())
most_prolific_author = find_keys_for_value(author_counts, max_times_authored)

print "The author with more papers is {0} with {1}.".format(most_prolific_author[0], max_times_authored)
