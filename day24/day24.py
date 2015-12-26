import sys

PACKAGES = (1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113)

WEIGHT = sum(PACKAGES) / 4

results = []
    
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print "sum(%s)=%s" % (partial, target)
        results.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 

def calc_quantum(serie):
    total = 1
    for i in serie:
        total *= i
    return total

def find_best():
    best_legroom = sys.maxint
    best_quantum = sys.maxint
    for result in results:
        if len(result) < best_legroom:
            best_legroom = len(result)
            best_quantum = calc_quantum(result)
        elif len(result) == best_legroom:
            q = calc_quantum(result)
            if q < best_quantum:
                best_quantum = q
    return (best_legroom, best_quantum)
 
if __name__ == "__main__":
    subset_sum(PACKAGES, WEIGHT)
    
    print find_best()
    