
# methods to eat vowels

def eat(str):
    msg = ''
    for s in str:
        if s not in 'aeiou':
            msg += s

    return msg

def eat2(str):
    msg = [s for s in str if s not in 'aeiou']
    return ''.join(msg)

s = eat("Paulo Leonardo Benatto")
s2 = eat2("Paulo Leonardo Benatto")
print s
print s2