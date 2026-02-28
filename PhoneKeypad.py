keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printCombination(combination,current_position,output,n):
    if current_position == n:
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[current_position]])):
        output.append(keypad[combination[current_position]][i])
        printCombination(combination,current_position+1,output,n)
        output.pop()
        if combination[current_position] == 0 or combination[current_position] == 1:
            return
combination = [4,3,4]
n = len(combination)
printCombination(combination,0,[],n)