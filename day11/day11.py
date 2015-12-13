
dupe_letters = ("aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", 
                "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", 
                "uu", "vv", "ww", "xx", "yy", "zz")

forbidden = ('i', 'o', 'l')

def val_rule_1(pw):
    current_val = 0
    for i in range(2, len(pw)):
        a,b,c = pw[i-2:i+1]
        if ord(a ) +1 == ord(b) == ord(c) - 1:
            return True
    return False

def val_rule_2(pw):
    return not any([c for c in pw if c in forbidden])

def val_rule_3(pw):
    pww = ''.join(pw)
    return len([c for c in dupe_letters if c in pww]) >= 2

def increment_letter(pw, position=1):
    if pw[-position] == 'z':
        pw[-position] = 'a'
        increment_letter(pw, position+1)
    else:
        pw[-position] = chr(ord(pw[-position]) + 1)
    return pw

def increment_password(pw):
    while not (val_rule_1(pw) and val_rule_2(pw) and val_rule_3(pw)):
        pw = increment_letter(pw)
    return ''.join(pw)

def main():
    pw = list('cqjxjnds')
    pw = increment_password(pw)
    pw = increment_letter(list(pw))
    print increment_password(pw)
    
if __name__ == '__main__':
    main()