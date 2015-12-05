
mapping = {
           "^": (0, 1),
           "v": (0, -1),
           "<": (-1, 0),
           ">": (1, 0)
           }

def read_data(filename):
    content = open(filename, "r").readlines()
    return content[0]

def add_house(visited_houses, currentpos):
    key = "x" + str(currentpos[0]) + "y" + str(currentpos[1])
    if visited_houses.has_key(key):
        visited_houses[key] += 1
    else:
        visited_houses[key] = 1
    
def calculate_how_many_houses(trajectory):
    currentpos = [0, 0]
    visited_houses = {}
    add_house(visited_houses, currentpos)
    
    for direction in trajectory:
        move = mapping.get(direction)
        currentpos[0] += move[0]
        currentpos[1] += move[1]
        add_house(visited_houses, currentpos)
        
    return len(visited_houses.keys())

def calculate_how_many_houses_with_robo_santa(trajectory):
    santapos = [0, 0]
    robopos = [0, 0]
    visited_houses = {}
    add_house(visited_houses, santapos)
    add_house(visited_houses, robopos)
    santa_move = True
    for direction in trajectory:
        move = mapping.get(direction)
        if santa_move:
            santapos[0] += move[0]
            santapos[1] += move[1]
            add_house(visited_houses, santapos)
        else:
            robopos[0] += move[0]
            robopos[1] += move[1]
            add_house(visited_houses, robopos)
        santa_move = not santa_move

    return len(visited_houses)

def main():
    trajectory = read_data("data1.txt")
    print calculate_how_many_houses(trajectory)
    print calculate_how_many_houses_with_robo_santa(trajectory)
    
if __name__ == "__main__":
    main()