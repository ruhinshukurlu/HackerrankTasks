# Simple Array Sum
# link : https://www.hackerrank.com/challenges/simple-array-sum/problem?h_r=profile

def simpleArraySum(arr):
    sum = 0
    for item in arr:
        sum += int(item)
    return  sum

size = int(input())
arr = input().split(' ')

sum = simpleArraySum(arr)
print(sum)