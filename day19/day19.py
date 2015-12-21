import re
import sys
MAX = sys.maxint

MEDECINE = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

def parse_replacements(lines):
    rep = []
    for line in lines:
        before, after = line.strip().split(" => ")
        rep.append((before, after))
    return rep

def find_atoms_in_medecine(medecine, atom):
    return [m.start() for m in re.finditer(atom, medecine)]

def find_combinations(medecine, replacements):
    combinations = []
    for after, before in replacements:
        for atom in find_atoms_in_medecine(medecine, before):
            newmed = medecine[:atom] + after + medecine[atom+len(before):]
            if not newmed in combinations:
                combinations.append(newmed)
    return combinations

def greedy_deconstruct(medecine, replacements, steps=1):
        
    combs = find_combinations(medecine, replacements)
    combs.sort(key=len)
    if "e" in combs:
        print steps+1
        raise Exception("GOT IT")
    for c in combs:
        print c, steps
        greedy_deconstruct(c, replacements, steps+1)        
    
def construct_molecule(replacements, molecule, build="e", steps=1):
    minsteps = MAX
    if steps > len(molecule):
        return minsteps
    if build in visited:
        return minsteps
    else:
        visited.append(build)
    
    for before, after in replacements:
        if before in build:
            for atom in find_atoms_in_medecine(build, before):
                newbuild = build[:atom] + after + build[atom+len(before):]
                if newbuild == molecule:
                    print steps
                    return steps 
                elif len(newbuild) < len(molecule):
                    print newbuild
                    stps = construct_molecule(replacements, molecule, newbuild, steps+1)
                    if minsteps > stps:
                        minsteps = stps 
    return minsteps                

visited = {}
loops = {}

def exc_decon(replacements):
    for comb in find_combinations(MEDECINE, replacements):
        visited.clear()
        loops.clear()
        try:
            deconstruct(replacements, "e", comb)
        except:
            continue
        
def deconstruct(replacements, molecule, build, steps=1):
    minsteps = MAX
    if steps > len(MEDECINE):
        return minsteps
    if build in visited.keys():
        if visited[build] > 1000:
            loops[visited[build]] = 1
            if loops >= 1000000000:
                raise Exception()
            return minsteps
        visited[build] += 1
    else:
        #visited.append(build)
        visited[build] = 1
    for before, after in replacements:
        if after in build:
            for atom in find_atoms_in_medecine(build, after):
                newbuild = build[:atom] + before + build[atom+len(after):]
                if newbuild == molecule:
                    print steps
                    import sys
                    sys.exit(0)
                    return steps 
                else:#if len(newbuild) < len(build):
                    print newbuild
                    stps = deconstruct(replacements, molecule, newbuild, steps+1)
                    if minsteps > stps:
                        minsteps = stps

    return minsteps                
    
def main():
    lines = open("data2.txt", "r").readlines()
    #lines.sort() 
    #lines.sort(key=len, reverse=True)
    replacements = parse_replacements(lines)
    #print construct_molecule(replacements, MEDECINE)
    #print deconstruct(replacements, "e", MEDECINE)
    print exc_decon(replacements)
    #print greedy_deconstruct(MEDECINE, replacements)
    #print replacements
    #print len(find_combinations(MEDECINE, replacements))
    
if __name__ == '__main__':
    main()