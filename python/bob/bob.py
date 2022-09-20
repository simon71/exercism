import re

def response(hey_bob):
    clean_hey_bob = re.sub(r"[\n\t\s]*","",hey_bob)
    if len(clean_hey_bob) == 0:
        return "Fine. Be that way!"
    elif clean_hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif clean_hey_bob[-1] == "?":
        return "Sure."
    elif clean_hey_bob.isupper() and hey_bob[-1] != "?":
        return "Whoa, chill out!"
    else: 
        return "Whatever."
