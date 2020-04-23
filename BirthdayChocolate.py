# Birthday chocolate
# link : https://www.hackerrank.com/challenges/the-birthday-bar/problem
def sum_list_elem(arr):
    list_sum = 0
    for elem in arr:
        list_sum += int(elem)
    return list_sum


size = int(input())
input_list = input().split(' ')
input_list_2 = input().split(' ')

sum = int(input_list_2[0])
count = int(input_list_2[1])

c=0

for i in range( size - count +1 ):
    part_list = input_list[i : i+count]
    if sum == sum_list_elem(part_list):
        c+=1

print(c)