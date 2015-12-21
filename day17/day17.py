import itertools

SIZES = sorted((50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40))
TOTAL = 150

MIN_CON = 1
MAX_CON = 10

combs = []
for i in range(MIN_CON, MAX_CON+1):
    for x in itertools.combinations(SIZES, i):
        if sum(x) == 150:# and x not in combs:
            combs.append(x)


    
print len(combs)

print len([x for x in itertools.combinations(SIZES, 4) if sum(x) == 150])
