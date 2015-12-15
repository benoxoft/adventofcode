import pprint

TOTAL = 2503

#Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.
def parse_reindeer(line):
    tokens = line.strip()[:-1].split()
    name = tokens[0]
    speed = int(tokens[3])
    flytime = int(tokens[6])
    resttime = int(tokens[-2])
    return (name, speed, flytime, resttime)

def calc_distance(speed, flytime, resttime, totaltime):
    rounds = totaltime / (flytime + resttime)
    distance = speed * flytime * rounds
    timeleft = totaltime - rounds * (flytime + resttime)
    if timeleft > flytime:
        distance += flytime * speed
    else:
        distance += timeleft * speed
    return distance

def find_fastest(lines):
    fastest = 0
    for line in lines:
        name, speed, flytime, resttime = parse_reindeer(line)
        distance = calc_distance(speed, flytime, resttime, TOTAL)
        if distance > fastest:
            fastest = distance
    return fastest

def create_reindeer(speed, flytime, resttime):
    def reindeer():
        while True:
            for i in range(0, flytime):
                yield speed
            for i in range(0, resttime):
                yield 0
    return reindeer

def race_points(lines):
    reindeers = []
    for line in lines:
        name, speed, flytime, resttime = parse_reindeer(line)
        reindeers.append([0, 0, create_reindeer(speed, flytime, resttime)(), name])
        
    for i in range(0, TOTAL):
        for r in reindeers:
            r[0] += r[2].next()

        fastest = 0
        for r in reindeers:
            if r[0] > fastest:
                fastest = r[0]
        for r in reindeers:
            if r[0] == fastest:
                r[1] += 1
        
    lead = reindeers[0]
    for r in reindeers:
        if r[1] > lead[1]:
            lead = r
    pprint.pprint(reindeers)
    return lead[1]

def main():
    lines = open("data1.txt", "r").readlines()
    print find_fastest(lines)
    print race_points(lines)
    
if __name__ == '__main__':
    main()
    