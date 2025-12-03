import sys
   
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
    #print(input_list)
    bank_sum = 0;
    
    for battery_banks in input_list:
        battery_sorted = sorted(battery_banks[:-1],reverse=True)
        #print(battery_sorted)
        first = battery_sorted[0]
        battery_sorted = sorted(battery_banks[battery_banks.index(first)+1:],reverse=True)
        #print(battery_sorted)
        temp_sum = int(str(first) + str(battery_sorted[0]))
        #print(temp_sum)
        bank_sum += temp_sum
        #if battery_sorted[0][1] < battery_sorted[1][1]:
        #    temp_sum = int(battery_sorted[0][0] + battery_sorted[1][0])
        #    print(f"Sum is {temp_sum}")
        #    bank_sum += temp_sum
        #else:
        #    temp_sum = int(battery_sorted[1][0] + battery_sorted[0][0])
        #    print(f"Sum is {temp_sum}")
        #    bank_sum += temp_sum

    print(f"Part 1 sum: {bank_sum}")

    bank_sum = 0;
    
    for battery_bank in input_list:
        #print(f"Battery Bank: {''.join(battery_bank)}")
        pick_index = 0
        start_window_index = -12
        chosen_nbrs = []
        maximum = max(battery_bank[:start_window_index])
        
        if maximum < battery_bank[start_window_index]:
            temp_sum = "".join(battery_bank[start_window_index:])
            # print(f"Added the following combination: {temp_sum}")
            bank_sum += int(temp_sum)
            pass
        
        pick_index = battery_bank.index(maximum,0,start_window_index)
        chosen_nbrs.append(maximum)
        #print(f"First")
        #print(chosen_nbrs)
        #print(f"Window Start: {start_window_index}")
        start_window_index += 1
        while(True):
            #print(f"Window Start: {start_window_index}")
            #print("Pick from")
            #print(battery_bank[pick_index + 1:start_window_index])
            #print("Window:")
            #print(battery_bank[start_window_index:])
            maximum = max(battery_bank[pick_index + 1:start_window_index])
            #print("Chosen nbrs")
            if maximum < battery_bank[start_window_index]:
                for nbr in battery_bank[start_window_index:]:
                    chosen_nbrs.append(nbr)
                #print(chosen_nbrs)
                break
            chosen_nbrs.append(maximum)
            if 12  + start_window_index - len(chosen_nbrs) == 0:
                for nbr in battery_bank[start_window_index:]:
                    chosen_nbrs.append(nbr)
                #print(chosen_nbrs)
                break
            pick_index = battery_bank.index(maximum,pick_index +1 ,start_window_index) 
            start_window_index += 1
            #print(" ".join(chosen_nbrs))
            if start_window_index == 0:
                break

        #print(" ".join(chosen_nbrs))
        bank_sum += int("".join(chosen_nbrs))
        
            



    print(f"Part 2 sum: {bank_sum}")

if __name__ == '__main__':
    main()
