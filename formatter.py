def arithmetic_arranger(li, x):


    return 

raw = ["32 + 698", "3801 - 3", "45 + 43", "123 + 49", "5 + 5"]

if len(raw) > 5:
    print("Error: Too many problems")
    quit()

for string in raw:
    ind = string.split()
    
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

    print(numb1, numb2)
    
    if op == "+":
        result = numb1 + numb2
    else:
        result = numb1 - numb2
    
    print(result)