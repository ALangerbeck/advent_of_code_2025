import sys



def main():
    input_list = []
    # Read input line by line
    for line in sys.stdin:
        if line.strip() == "":
            pass
        else:
            #input_list.append(line.split())
            sublist = []
            for i,item in enumerate(line.strip()):
             sublist.append((item,i))
            input_list.append(sublist)
    #print(input_list)
    bank_sum = 0;

    for battery_banks in input_list:
        battery_sorted = sorted(battery_banks, key=lambda x: x[0], reverse=True)
        if battery_sorted[0][1] < battery_sorted[1][1]:
            temp_sum = int(battery_sorted[0][0] + battery_sorted[1][0])
            print(f"Sum is {temp_sum}")
            bank_sum += temp_sum
        else:
            temp_sum = int(battery_sorted[1][0] + battery_sorted[0][0])
            print(f"Sum is {temp_sum}")
            bank_sum += temp_sum

    print(f"Part 1 sum: {bank_sum}")


if __name__ == '__main__':
    main()
