import string

def is_pangram(sentence):
    return not bool(set(string.ascii_lowercase) - set(sentence.lower()))

"""
first create 2 set's one of a-z and one using the sentence
a set is {a,b,c,d,e}
then we can subtract the alphabet set from the sentence and see what's left
when wrapped in a bool it will return false if nothing is left and true if there is
so we add the not before the bool so it returns true if nothing is left
"""

