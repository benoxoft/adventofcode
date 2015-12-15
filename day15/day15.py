
#capacity durability flavor texture calories
Sprinkles = (2, 0, -2, 0, 3)
Butterscotch = (0, 5, -3, 0, 3)
Chocolate = (0, 0, 5, -1, 8)
Candy = (0, -1, 0, 5, 8)

TEASPOONS = 100

def find_bestest():
    bestest = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if i+j > 100:
                break
            for k in range(0, 100):
                if i+j+k > 100:
                    break
                for l in range(0, 100):
                    if i+j+k+l > 100:
                        break
                    if i+j+k+l < 100:
                        continue
                    cal = calculate_calories(i, j, k, l)
                    if cal != 500:
                        continue
                    p = calculate_potential(i, j, k, l)
                    if p > bestest:
                        bestest = p
    return bestest
    

def calculate_potential(i, j, k, l):
    return calculate_capacity(i, j, k, l) * calculate_durability(i, j, k, l) * calculate_flavor(i, j, k, l) * calculate_texture(i, j, k, l)

def calculate_capacity(i, j, k, l):
    c = Sprinkles[0] * i + Butterscotch[0] * j + Chocolate[0] * k + Candy[0] * l
    if c < 0:
        return 0
    else:
        return c
    
def calculate_durability(i, j, k, l):
    c = Sprinkles[1] * i + Butterscotch[1] * j + Chocolate[1] * k + Candy[1] * l
    if c < 0:
        return 0
    else:
        return c
    
def calculate_flavor(i, j, k, l):
    c = Sprinkles[2] * i + Butterscotch[2] * j + Chocolate[2] * k + Candy[2] * l
    if c < 0:
        return 0
    else:
        return c
    
def calculate_texture(i, j, k, l):
    c = Sprinkles[3] * i + Butterscotch[3] * j + Chocolate[3] * k + Candy[3] * l
    if c < 0:
        return 0
    else:
        return c
    
def calculate_calories(i, j, k, l):
    c = Sprinkles[4] * i + Butterscotch[4] * j + Chocolate[4] * k + Candy[4] * l
    if c < 0:
        return 0
    else:
        return c
    
def main():
    print find_bestest()
    
if __name__ == '__main__':
    main()
    