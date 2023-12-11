""" 
Practice Question 2: Filter and Count

Task:

Write a function filter_and_count that takes a list of strings and a substring. 
The function should return the count of strings in the list that contain the given substring.
"""

def filter_and_count(strings, substring):
    count = 0
    for string in strings:
        if substring in string:
            count += 1

    return count