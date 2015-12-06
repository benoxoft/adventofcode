
lights = {}

def key(x, y):
    return "x" + str(x) + "y" + str(y)

def turn_on(x, y):
    k = key(x, y)
    if lights.has_key(k):
        lights[k] += 1
    else:
        lights[k] = 1

def turn_off(x, y):
    k = key(x, y)
    if lights.has_key(k):
        lights[k] -= 1
        if lights[k] == 0:
            del lights[k]

def toggle(x, y):
    turn_on(x, y)
    turn_on(x, y)

functions = {"turn on": turn_on, "turn off": turn_off, "toggle": toggle}

#turn on 774,14 through 977,877
def execute_command(command):
    for s, func in functions.items():
        if s in command:
            tokens = command.split(" ")
            x1, y1 = tokens[-3].split(",")
            x2, y2 = tokens[-1].split(",")
            for x in xrange(int(x1), int(x2) + 1):
                for y in xrange(int(y1), int(y2) + 1):
                    func(x, y)

def read_data(filename):
    lines = open(filename, "r").readlines()
    return lines

def main():
    lines = read_data("data1.txt")
    for line in lines:
        execute_command(line)
    print sum(lights.values())
    
if __name__ == "__main__":
    main()
    