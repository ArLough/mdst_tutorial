"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x%2 ==0:
        return False
    else:
        return True
    """
    returns True if x is odd and False otherwise
    """


def is_palindrome(word):
    s=""
    for i in reversed(word):
        s = i
    
    if s == word:
        return True
    else:
        return False
   
        
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    l = list()
    for i in numlist:
        if i%2 != 0:
            l.append(i)
    
    return l
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    l = text.split(" ")
    d = dict()
    for i in l:
        i = i.lower()
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1

    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
