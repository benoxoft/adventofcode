from numpy import uint16

def RSHIFT(a, b):
    return a >> b

def LSHIFT(a, b):
    return a << b

def OR(a, b):
    return a | b

def AND(a, b):
    return a & b

def NOT(a):
    return ~a 

operators = {
             "RSHIFT" : RSHIFT,
             "LSHIFT" : LSHIFT,
             "OR" : OR,
             "AND" : AND,
             "NOT" : NOT
}

def wire_value(token, solved_wires):
        if str.isdigit(token):
            return uint16(token)
        elif token in solved_wires.keys():
            return uint16(solved_wires.get(token))
        else:
            return None
        
def solve_wire(operation, solved_wires):
    tokens = operation.split(" ")
    if len(tokens) == 1:
        val = wire_value(tokens[0], solved_wires)
        if val is not None:
            return val
        
    elif len(tokens) == 2:
        a = wire_value(tokens[1], solved_wires)
        if a is not None:
            return operators.get(tokens[0])(a)
    elif len(tokens) == 3:
        a = wire_value(tokens[0], solved_wires)
        b = wire_value(tokens[2], solved_wires)
        if a is not None and b is not None:
            return operators.get(tokens[1])(a, b)
    return None

def solve_circuit(wires):
    solved_wires = {}
    while len(wires) > 0:
        size = len(wires)
        for i in range(0, len(wires)):
            wire = wires[i].strip()
            operation, result = wire.split(" -> ")
            result = result.strip()
            answer = solve_wire(operation, solved_wires)
            if answer is not None:
                print "SOLVED", wire, "FOR", answer
                solved_wires[result.strip()] = answer
                del wires[i]
                break
        if size == len(wires) and size > 0:
            import pprint
            pprint.pprint(wires)
            print "len:", size
            raise Exception("Unsolvable")
    return solved_wires

def main():
    wires = open("data1.txt", "r").readlines()
    result = solve_circuit(wires)
    print result
    print result['a']
    
if __name__ == '__main__':
    main()
    