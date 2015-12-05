
dupe_letters = ("aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", 
                "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", 
                "uu", "vv", "ww", "xx", "yy", "zz")

naughty_letters = ("ab", "cd", "pq", "xy")

vowels = ("a", "e", "i", "o", "u")

NAUGHTY = "naughty"
NICE = "nice"

def judge_word_part1(word):
    if any([n for n in naughty_letters if n in word]):
        return NAUGHTY
    
    if len([c for c in word if c in vowels]) < 3:
        return NAUGHTY
    
    if not any([d for d in dupe_letters if d in word]):
        return NAUGHTY
    
    return NICE

def judge_word_part2(word):
    dupe_count = {}
    last_dupe = ""
    tl_repeat = False
    
    for i in xrange(0, len(word)):
        if i < len(word) - 1:
            pair = word[i:i+2]
            if pair != last_dupe:
                if dupe_count.has_key(pair):
                    dupe_count[pair] += 1
                else:
                    dupe_count[pair] = 1
            if pair != last_dupe and pair in dupe_letters:
                last_dupe = pair
            else:
                last_dupe = ""
                
        if i < len(word) - 2:
            tl = word[i:i+3]
            if tl[0] == tl[-1]:
                tl_repeat = True
             
    if tl_repeat and any([v for v in dupe_count.values() if v >= 2]):
        return NICE
    else:
        return NAUGHTY        
    
def read_data(filename):
    content = open("data1.txt", "r").readlines()
    return content

def main():
    lines = read_data("data1.txt")
    print len([word for word in lines if judge_word_part1(word) == NICE])
    print len([word for word in lines if judge_word_part2(word) == NICE])

if __name__ == "__main__":
    main()
    