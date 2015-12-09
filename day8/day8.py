import json

lines = open("data1.txt", "r").readlines()
size = 0 
for line in lines:
    line = line.strip()
    size += len(json.dumps(line)) - len(line) 
print size
