#Sue 367: children: 4, vizslas: 5, akitas: 4

SUE_DATA = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1    
}

def parse_line(line):
    line = line.strip()
    tokens = line.split(" ")
    sue_no = int(tokens[1][:-1])
    data = {}
    for i in range(2, len(tokens), 2):
        key = tokens[i][:-1]
        value = int(tokens[i+1].replace(",", ""))
        data[key] = value
    return (sue_no, data)

def sort_sues(lines):
    sues = []
    for line in lines:
        sue_no, data = parse_line(line)
        match = True
        for key, value in data.items():
            if key in SUE_DATA.keys():
                if key in ("cats", "trees"):
                    if SUE_DATA[key] >= value or value == 0:
                        match = False
                        break
                elif key in ("pomeranians", "goldfish"):
                    if SUE_DATA[key] <= value or value == 0:
                        match = False
                        break
                elif SUE_DATA[key] != value:
                    match = False
                    break
            else:
                match = False
                break
        if match:
            print sue_no, data

def main():
    lines = open("data1.txt", "r").readlines()
    sort_sues(lines)

if __name__ == '__main__':
    main()
