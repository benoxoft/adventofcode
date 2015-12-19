
ON = "#"
OFF = "."

def parse_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid

def get_neighbor_values(grid, xl, yl):
    values = []
    for x, y in [(xl+i,yl+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if -1 < x < len(grid) and -1 < y < len(grid):
            values.append(grid[x][y])
        else:
            values.append(OFF)
    return values

def decide_switch(values, current_light):
    on_neighbors = len([x for x in values if x == ON])
    
    if current_light == ON and on_neighbors in (2, 3):
        return ON
    elif current_light == ON:
        return OFF
    elif current_light == OFF and on_neighbors == 3:
        return ON
    else:
        return OFF

def change_light_grid(grid):
    new_grid = []
    for x in range(0, len(grid)):
        new_grid.append([])
        for y in range(0, len(grid)):
            if x in (0 , len(grid) -1) and y in (0 , len(grid) -1):
                new_grid[x].append(ON)
                continue
            current_light = grid[x][y]
            neighbors = get_neighbor_values(grid, x, y)
            new_grid[x].append(decide_switch(neighbors, current_light))
            assert grid[x][y] == current_light
    return new_grid

def flash_lights(grid, count):
    for i in range(0, count):
        grid = change_light_grid(grid)
    return grid

def main():
    lines = open("data1.txt", "r").readlines()
    grid = parse_grid(lines)
    grid = flash_lights(grid, 100)
    print len([y for x in grid for y in x if y == ON])
    
if __name__ == '__main__':
    main()