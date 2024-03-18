#Lucas Vandenakker

#CS175L

#AverageFromInput


def main():
    name_file = open('numbers.txt', 'r')
    total = 0
    count = 1
    for line in name_file:
        
        num = float(line)
        total += num
        print("I read in", count, "number(s) Current number is:", num,  "Total is:")
        print(total)

        count+=1
       

    avg = total/3
    print("Average:", avg)


if __name__ == '__main__':
    main()
