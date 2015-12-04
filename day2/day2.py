
def calculate_paper(l, w, h):
    subtotal = (2*l*w) + (2*w*h) + (2*h*l)
    x1, x2, _ = sorted((l, w, h))
    extra = x1 * x2
    return subtotal + extra

def calculate_ribbon(l, w, h):
    x1, x2, _ = sorted((l, w, h))
    ribbon = x1 + x1 + x2 + x2
    bow = l * w * h
    return bow + ribbon

def read_data(filename):
    content = open(filename, "r").readlines()
    return [line.split("x") for line in content]

def main():
    size = 0
    for l, w, h in read_data("data1.txt"):
        size += calculate_paper(int(l), int(w), int(h))
    print size

    size = 0
    for l, w, h in read_data("data2.txt"):
        size += calculate_ribbon(int(l), int(w), int(h))
    print size
    
if __name__ == "__main__":
    main()
    