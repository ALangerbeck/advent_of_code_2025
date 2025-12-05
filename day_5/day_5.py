import sys

def print_grid(input_list):
    for row in input_list:
        print("".join(row))

def main():
    date_set = set()
    temp_set = set()
    id_list = []
    # Read input line by line
    for line in sys.stdin:
        if line.strip() == "":
            break
        else:
            range_a = line.strip().split("-")
            temp_set = set(range(int(range_a[0]),int(range_a[1])+1))
            print(f"Adding {temp_set}")
            date_set = date_set.union(temp_set)
    for line in sys.stdin:
        id_list.append(int(line.strip()))
    
    print(id_list)
    print(date_set)
    
    good_items = 0

    for item in id_list:
        if item in date_set:
            good_items += 1
    
    print(f"Part 1 good items: {good_items}")
if __name__ == '__main__':
    main()
