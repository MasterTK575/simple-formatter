

# ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]


def arithmetic_arranger(li, x="False"):
    # error checking
    if len(li) > 5:
        # you need to return here so that the test recognizes it
        # printing doesn't work
        # returning also stops the function from continuing
        return "Error: Too many problems."

    # create some lists
    numbers1 = list()
    numbers2 = list()
    operators = list()
    results = list()
    totlen = list()

    # for each string in the list, aka. each computation in ""
    for string in li:
        ind = string.split()
        
        # a bunch of error checking
        try:
            numb1 = int(ind[0])
            numb2 = int(ind[2])
        except:
            return "Error: Numbers must only contain digits."
           
        if len(str(numb1)) > 4 or len(str(numb2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        op = ind[1]
        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."

        # calculating the results
        if op == "+":
            result = numb1 + numb2
        else:
            result = numb1 - numb2

        # finding out the max lenght of each problem
        # if number 1 is the biggest, use it as a proxy for total line length
        # else use number 2
        lennumb1 = len(str(numb1))
        lennumb2 = len(str(numb2))
        if lennumb1 >= lennumb2:
            totlen.append(lennumb1 + 2)
        else:
            totlen.append(lennumb2 + 2)

        # print(totlen)
        
        # creating lists for each part of the problem
        numbers1.append(numb1)
        numbers2.append(numb2)
        results.append(result)
        operators.append(op)

    
    # print the first line
    # use str.rjust() to center the text on the right
    count = 0
    line1 = ""
    for number in numbers1:
        line = str(number).rjust(totlen[count])
        if count == 0:
            line1 = line1 + line
        else:
            line1 = line1 + "    " + line
        count = count + 1
    line1 = line1 + "\n"


    # print the second line
    count = 0
    line2 = ""
    for number in numbers2:
        # .rjust(totlen[count] - 1) to account for the operator
        line = operators[count] + str(number).rjust(totlen[count] - 1)
        if count == 0:
            line2 = line2 + line
        else:
            line2 = line2 + "    " + line
        count = count + 1
    line2 = line2 + "\n"
    # print(line2)

    # print line 3
    # create the ---- lines by looping for the total lenght of the line
    count = 0
    line3 = ""
    for number in numbers1:
        countsmall = totlen[count]
        # redefine linesmall each time to make sure it doesn't stack
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
    # print(line3)


    count = 0
    line4 = ""
    for number in results:
        line = str(number).rjust(totlen[count])
        if count == 0:
            line4 = line4 + line
        else:
            line4 = line4 + "    " + line
        count = count + 1
    # print(line4)

    if x == True:
        toreturn = line1 + line2 + line3 + "\n" + line4
        return toreturn
    else:
        toreturn = line1 + line2 + line3
        return toreturn


print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
