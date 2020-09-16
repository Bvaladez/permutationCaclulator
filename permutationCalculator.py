INTS = [1,2,3,4,5,6,7,8,9]

def getUserInput():
    userInput = input("Type a number 1-9: ")
    
    return userInput

def factorial(number):
    factorial = 1
    for i in range(number):
        factorial *= i + 1

    return factorial

def printPermutations(permutations):
    s = ''
    for p in permutations:
        for n in p:
            s += str(n)
        print(s)
        s = ''

    return 0


'''
recieves a list of digits
returns a list of all permutations in lexicographical order
'''
def computePermutations(digits):
    permutations = []
    count = 0
    p = digits[:]
    combinations = factorial(digits[-1])
    

    n = len(digits) - 1
    j = n - 1
   
    # put the first permutation in the list before calculating next
    permutations.append(p[:]) 
    while count < combinations - 1:
        
        j = n - 1
        count += 1

        while p[j] > p[j + 1]:
            j -= 1
        k = n
        while p[j] > p[k]:
            k -= 1
        # interchange p[j] and p[k]
        temp = p[j]
        p[j] = p[k]
        p[k] = temp

        r = n
        s = j + 1
        while r > s:
            # interchange p[r] and p[s]
            temp = p[r]
            p[r] = p[s]
            p[s] = temp
            r -= 1
            s += 1
        permutations.append(p[:])
    
    print("combinations:", factorial(digits[-1]))
    print("count:", count)
    print()

    return permutations


def main():
    rangeToPermute = int(getUserInput())
    # create a list of all the numbers we can use to permute
    numbersToPermute = INTS[:rangeToPermute]
    permutations = computePermutations(numbersToPermute)
    
    printPermutations(permutations)
    
    return 0



    

if __name__ == "__main__":
    main()