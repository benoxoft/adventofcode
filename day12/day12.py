import itertools, pprint, json

def sum_all_ints(data):
    summ = 0
    
    while len(data) > 0:
        print "new"
        to_delete = []
        for x in data:
            if isinstance(x, int):
                print x
                summ += x
                to_delete.append(x)
                has_int = True
            elif isinstance(x, unicode):
                to_delete.append(x)
            elif isinstance(x, dict):
                red = False
                for z in x.values():
                    if z == 'red':
                        red = True
                if red:
                    to_delete.append(x)
                else:
                    data[data.index(x)] = x.values()
        for x in to_delete:
            del data[data.index(x)]
        try:
            data = [x for x in itertools.chain.from_iterable(data)]
        except:
            pprint.pprint(data)
            raise
    return summ
    
def main():
    data = json.load(open("data1.json", "r"))
    print sum_all_ints(data)
    
if __name__ == '__main__':
    main()