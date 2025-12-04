import sys

def print_grid(input_list):
    for row in input_list:
        print("".join(row))

def main():
    input_list = []
    # Read input line by line
    for line in sys.stdin:
        if line.strip() == "":
            pass
        else:
            input_list.append(list(line.strip()))
            #sublist = []
            #for i,item in enumerate(line.strip()):
            # sublist.append((item,i))
            #input_list.append(sublist)
    #print(input)
    #print(input_list)
    
    a_bales = 0;

    for y,row in enumerate(input_list):
        for x, spot in enumerate(row):
            
            neigbours = ""
            if(spot == "@"): 
            
                #Corners
                    if ((y == 0 and x == 0) or (y==0 and x == (len(row)-1)) or (y==(len(input_list)-1) and x==0)
                            or (y==(len(input_list)-1) and x == (len(row)-1))):
                        a_bales += 1
            
                #Horizontal sides
                    elif(y == 0 and (x > 0 and x < len(row) -1 )): 
                        neigbours = input_list[y][x-1] + input_list[y+1][x-1] + input_list[y+1][x] + input_list[y+1][x+1] + input_list[y][x+1]
                    
                    elif(y == len(row) - 1 and (x > 0 and x < len(row) -1 )):
                        neigbours = input_list[y][x-1] + input_list[y-1][x-1] + input_list[y-1][x] + input_list[y-1][x+1] + input_list[y][x+1]
                                        
                #Vertical sides
                    elif(x == len(input_list) - 1 and (y > 0 and y < len(input_list) -1 )):
                        neigbours = input_list[y-1][x] + input_list[y-1][x-1] + input_list[y][x-1] + input_list[y+1][x-1] + input_list[y+1][x]
                    elif(x == 0 and (y > 0 and y < len(input_list) -1 )):
                        neigbours = input_list[y-1][x] + input_list[y-1][x+1] + input_list[y][x+1] + input_list[y+1][x+1] + input_list[y+1][x]
                    else:
                        neigbours = (input_list[y-1][x-1] + input_list[y-1][x] + input_list[y-1][x+1] +
                                    input_list[y][x-1] + input_list[y][x+1] +
                                    input_list[y+1][x-1] + input_list[y+1][x] + input_list[y+1][x+1])
 
                    if(neigbours != "" and neigbours.count("@") < 4):
                            a_bales += 1

                #The rest
            else:
                pass

    print(f"Part 1: {a_bales}")
    
    #print("")
    #print_grid(input_list)
    a_bales = 0;
    remove = []
    while(True):
        for y,row in enumerate(input_list):
            for x, spot in enumerate(row):
            
                neigbours = ""
                if(spot == "@"): 
            
                    #Corners
                        if ((y == 0 and x == 0) or (y==0 and x == (len(row)-1)) or (y==(len(input_list)-1) and x==0)
                                or (y==(len(input_list)-1) and x == (len(row)-1))):
                            a_bales += 1
                            remove.append((y,x))
            
                        #Horizontal sides
                        elif(y == 0 and (x > 0 and x < len(row) -1 )): 
                            neigbours = input_list[y][x-1] + input_list[y+1][x-1] + input_list[y+1][x] + input_list[y+1][x+1] + input_list[y][x+1]
                    
                        elif(y == len(row) - 1 and (x > 0 and x < len(row) -1 )):
                            neigbours = input_list[y][x-1] + input_list[y-1][x-1] + input_list[y-1][x] + input_list[y-1][x+1] + input_list[y][x+1]
                                        
                        #Vertical sides
                        elif(x == len(input_list) - 1 and (y > 0 and y < len(input_list) -1 )):
                            neigbours = input_list[y-1][x] + input_list[y-1][x-1] + input_list[y][x-1] + input_list[y+1][x-1] + input_list[y+1][x]
                        elif(x == 0 and (y > 0 and y < len(input_list) -1 )):
                            neigbours = input_list[y-1][x] + input_list[y-1][x+1] + input_list[y][x+1] + input_list[y+1][x+1] + input_list[y+1][x]
                        else:
                            neigbours = (input_list[y-1][x-1] + input_list[y-1][x] + input_list[y-1][x+1] +
                                    input_list[y][x-1] + input_list[y][x+1] +
                                    input_list[y+1][x-1] + input_list[y+1][x] + input_list[y+1][x+1])
 
                        if(neigbours != "" and neigbours.count("@") < 4):
                            a_bales += 1
                            remove.append((y,x))
                else:
                    pass
        if (not remove):
            break
        while(remove):
            (y,x) = remove.pop()
            input_list[y][x] = '.'
        #print("")
        #print_grid(input_list)
                    
    print(f"Part 2: {a_bales}")
if __name__ == '__main__':
    main()
