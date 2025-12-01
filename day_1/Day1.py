import sys



def main():
    input_list = []
    # Read input line by line
    for line in sys.stdin:
        if "|" in line:
            (before, after) = line.split("|")
            tpl = (int(before), int(after))
            rules.append(tpl)
        elif line.strip() == "":
            pass
        else:
            input_list.append(line)

    position = 50
    cnt = 0
    pass_count = 0

    for inst in input_list:
        
        if inst[0] == 'L':
            start_pos = position
            change = (position - int(inst[1:]))
            #print(f"debug: {change}")
            position = change % 100
        else:
            change = (position + int(inst[1:]))
            #print(f"debug: {change}")
            position = change % 100
        if position == 0:
            cnt += 1
            
        #print(position)
    print(f"Part 1: {cnt}")
    
    position = 50;
    cnt = 0
    for inst in input_list:
        for i in range(int(inst[1:])):
            if inst[0] == 'L':
                position = (position - 1) % 100
                #print(f"Intermediate pos {position}")
                if(position == 0):
                    cnt += 1 
            else:
                position = (position + 1) % 100
                if(position == 0):
                    cnt += 1 
        print(f"Debug Step 2: {position}")
    print(f"Part 2: {cnt}")


if __name__ == '__main__':
    main()