import itertools
import sys

# AlphaCentauri to Arbre = 74
#{"AlphaCentauri": {"Arbre" : 74}}
#{"Arbre": {"AlphaCentauri" : 74}}

def parse_road(road_string):
    tokens = road_string.strip().split(" ")
    return (tokens[0], tokens[2], int(tokens[4]))

def build_dict(roads):
    rdict = {}
    for road_string in roads:
        city1, city2, distance = parse_road(road_string)
        add_cities_to_dict(rdict, city1, city2, distance)
        add_cities_to_dict(rdict, city2, city1, distance)
    return rdict

def add_cities_to_dict(rdict, city1, city2, distance):
    if rdict.has_key(city1):
        if not rdict[city1].has_key(city2):
            rdict[city1][city2] = distance
    else:
        rdict[city1] = {city2: distance}
                    
def find_smallest(roads):
    rdict = build_dict(roads)
    
    min_size = 0
    for travel in itertools.permutations(rdict.keys(), len(rdict)):
        distance = 0
        for i in range(0, len(travel)-1):
            city1 = travel[i]
            city2 = travel[i+1]
            distance += rdict[city1][city2]
        print distance
        if distance > min_size:
            min_size = distance
    return min_size
        
def main():
    roads = open("data1.txt", "r").readlines()
    print find_smallest(roads)
    
if __name__ == "__main__":
    main()
    
