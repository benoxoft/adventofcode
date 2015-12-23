
#hlf r sets register r to half its current value, then continues with the next instruction.
#tpl r sets register r to triple its current value, then continues with the next instruction.
#inc r increments register r, adding 1 to it, then continues with the next instruction.
#jmp offset is a jump; it continues with the instruction offset away relative to itself.
#jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
#jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

regs = {"a" : 1, "b" : 0, "c" : 0}

def hlf(r):
    regs[r] /= 2

def tpl(r):
    regs[r] *= 3

def inc(r):
    regs[r] += 1

def jmp(offset):
    regs["c"] += offset

def jie(r, offset):
    if regs[r] % 2 == 0:
        regs["c"] += offset 

def jio(r, offset):
    if regs[r] == 1:
        regs["c"] += offset
    
instructions = {"hlf" : hlf, "tpl" : tpl, "inc" : inc, "jmp" : jmp, "jie" : jie, "jio" : jio}

def parse_program(line):
    tokens = line.strip().split()
    for i in range(0, len(tokens)):
        tokens[i] = tokens[i].replace(",", "")
        try:
            tokens[i] = int(tokens[i])
        except:
            pass
    return tokens
        
def build_prog():
    prog = []
    for line in open("data1.txt", "r").readlines():
        p = parse_program(line)
        prog.append(p)
    return prog

def run_program(prog):
    while regs["c"] < len(prog):
        cursor = regs["c"]
        line = prog[regs["c"]]
        instructions[line[0]](*line[1:])
        if regs["c"] == cursor:
            regs["c"]+=1
        print line, regs
        
def main():
    prog = build_prog()
    run_program(prog)
    print regs 
    
if __name__ == "__main__":
    main()