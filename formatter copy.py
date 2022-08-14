

# ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]


def arithmetic_arranger(li, x="False"):
    # error checking
    if len(li) > 5:
        print("Error: Too many problems")
        quit()

    # create some lists
    numbers1 = list()
    numbers2 = list()
    operators = list()
    results = list()
    totlen = list()

    # for each string in the list
    for string in li:
        ind = string.split()
        
        # a bunch of error checking
        try:
            numb1 = int(ind[0])
            numb2 = int(ind[2])
        except:
            print("Error: Numbers must only contain digits.")
            quit()
        if len(str(numb1)) > 4 or len(str(numb2)) > 4:
            print("Erorr: Numbers cannot have more than 4 digits.")
            quit()
        op = ind[1]
        if op != "+" and op != "-":
            print("Error: Operator must be '+' or '-'.")

        # calculating the results
        if op == "+":
            result = numb1 + numb2
        else:
            result = numb1 - numb2

        # finding out the max lenght of each problem
        # the second numbers have at least 2 extra characters due to the operator and min. one space being in the same line
        if len(str(numb2)) == 4:
            lennumb2 = 6
        else:
            lennumb2 = len(str(numb2)) + 3

        problem = (len(str(numb1)), lennumb2, len(str(result)))
        totlen.append((max(problem)))
        
        # creating lists for each part of the problem
        numbers1.append(numb1)
        numbers2.append(numb2)
        results.append(result)
        operators.append(op)

    
    # print the first line
    count = 0
    line1 = ""
    for number in numbers1:
        # calculate the diff between total lenght and lenght of the number
        # that way we know how many spaces to add extra
        line = str(number).rjust(totlen[count])
        if count == 0:
            line1 = line1 + line
        else:
            line1 = line1 + "    " + line
        count = count + 1
    print(line1)

    # print the second line
    count = 0
    line2 = ""
    for number in numbers2:
        numblen = len(str(number))
        diff = totlen[count] - numblen
        if len(str(number)) == 4:
            print(" "*(3 + diff - 2), operators[count], number, end="")
        else:
            print(" "*(3 + diff - 3), operators[count], "", number, end="")
        count = count + 1
    print()

    # print line 3
    count = 0
    line3 = ""
    for number in numbers1:
        countsmall = totlen[count]
        linesmall = ""
        while countsmall > 0:
            line = "-"
            linesmall = linesmall + line
            countsmall = countsmall - 1

        if count == 0:
            line3 = linesmall
        else:
            line3 = line3 + "    " + linesmall
        count = count + 1
    print(line3)

    if x == True:
        count = 0
        for number in results:
            numblen = len(str(number))
            diff = totlen[count] - numblen
            print(" "*(3 + diff),number,end="")
            count = count + 1
        print()


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
