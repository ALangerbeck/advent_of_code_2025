import sys



def main():
    input_list = []
    # Read input line by line
    for line in sys.stdin:
        for span in line.strip().split(","):
            input_list.append(span.split("-"))
        

    #print(input_list)

    id_sum = 0

    for span in input_list:
        for id in range(int(span[0]),int(span[1])+1):
            #print(f"\nid: {id}")
            for character_combs in range(len(str(id))):
                substring = str(id)[:character_combs]
                if str(id).replace(substring,"",2) == "":
                    id_sum += id
                    #print(f"id: {id} is false") 
                    break
                
    print(f"Part 1 sum is {id_sum}")
    
    for span in input_list:
        for id in range(int(span[0]),int(span[1])+1):
            #print(f"\nid: {id}")
            for character_combs in range(len(str(id))):
                substring = str(id)[:character_combs]
                if str(id).replace(substring,"") == "":
                    id_sum += id
                    #print(f"id: {id} is false") 
                    break
                
    print(f"Part 2 sum is {id_sum}")
    

if __name__ == '__main__':
    main()
