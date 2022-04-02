def isprime(number):
    if number==2 or number==3:
        return True
    if number%2==0 or number<2:
        return False
    for n in range(3,int(number**0.5)+1,2):   
        if number%n==0:
            return False   
    return True
    
# print(isprime(11)) // for prime check

def maxPathSumTriangle(arr):
    newlist = [row[:] for row in arr]
    print(newlist)
    for row in range(len(arr)-2, -1, -1):
        for col in range(len(arr[row])):
            if (isprime(newlist[row][col]) or (isprime(newlist[row+1][col]) and isprime(newlist[row+1][col+1]))):
                continue
            elif (isprime(newlist[row+1][col]) == False and isprime(newlist[row+1][col+1]) == False):
                 arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])
            elif (isprime(newlist[row+1][col]) == False and isprime(newlist[row+1][col+1]) == True):
                arr[row][col] += arr[row+1][col]
            elif (isprime(newlist[row+1][col]) == True and isprime(newlist[row+1][col+1]) == False):
                arr[row][col] += arr[row+1][col+1]
    return arr[0][0]

with open("input.txt") as f:
    arr = []
    for line in f:
        arr.append(list(map(int, line.split(" "))))
    print("Maximum Path is: " maxPathSumTriangle(arr))
