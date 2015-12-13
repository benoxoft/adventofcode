import itertools

GUESTS = ("Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory", "Me")

#David would gain 75 happiness units by sitting next to George.
def parse_line(line):
    tokens = line.strip()[:-1].split(" ")
    guest1 = tokens[0]
    verb = tokens[2]
    amount = int(tokens[3])
    guest2 = tokens[-1]
    if verb == "lose":
        amount = -amount
    return (guest1, guest2, amount)

def create_dict(lines):
    moods = {}
    for line in lines:
        guest1, guest2, amount = parse_line(line)
        if moods.has_key(guest1):
            moods[guest1][guest2] = amount
        else:
            moods[guest1] = {}
            moods[guest1][guest2] = amount
    moods["Me"] = {}
    for guest in GUESTS:
        moods["Me"][guest] = 0
        moods[guest]["Me"] = 0
        
    return moods

def calculate_mood(seating, moods):
    mood = 0
    for i in range(0, len(seating)):
        guest1 = seating[i]
        if i == len(seating) - 1:
            guest2 = seating[0]
        else:
            guest2 = seating[i+1]
        mood += moods[guest1][guest2]
        mood += moods[guest2][guest1]
    return mood

def find_best_seating(lines):
    moods = create_dict(lines)
    best_mood = 0
    for seating in itertools.permutations(GUESTS):
        mood = calculate_mood(seating, moods)
        if mood > best_mood:
            best_mood = mood 
    return best_mood

def main():
    lines = open("data1.txt", "r").readlines()
    print find_best_seating(lines)
    
if __name__ == "__main__":
    main()
    