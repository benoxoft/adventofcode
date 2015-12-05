import md5

MAX_LOOP = 1000 * 1000 * 10

def find_hash(key, zeroes=5):
    for i in xrange(0, MAX_LOOP):
        hash = md5.md5(key + str(i)).hexdigest()
        if hash[0:zeroes] == "".ljust(zeroes, "0"):
            return i
    raise Exception("Could not find a hash")

def main():
    print find_hash("iwrupvqb", 6)
    
if __name__ == "__main__":
    main()