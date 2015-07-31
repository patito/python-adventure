

def eat_vowels(str):
    msg = ''
    for s in str:
        if s not in 'aeiou':
            msg += s

    return msg

s = eat_vowels("Apple Sauce")
print s