
def look_and_say(input):
    current = input[0]
    count = 0
    ret = ""
    for c in input:
        if current == c:
            count += 1
        else:
            ret += str(count) + current
            count = 1 
            current = c
    ret += str(count) + current 
    return ret

def main():
    input = "1321131112"
    for i in range(0, 50):
        input = look_and_say(input)
    print len(input)
    
if __name__ == "__main__":
    main()
    