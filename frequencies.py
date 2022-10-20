"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        frequencies[item] = items.count(item)
    # Your code goes here
    return frequencies
