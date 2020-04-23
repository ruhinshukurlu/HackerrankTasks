# Divisible Sum Pairs
# link : https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=profile

list_1 = input().split(' ')
size = int(list_1[0])
k = int(list_1[1])
c=0
num_list = input().split(' ')

for i in range(size):
    for j in range(i+1,size):
        list_sum =  lambda a,b : a+b
        sum = list_sum( int(num_list[i]), int(num_list[j]))
        if sum % k == 0:
            c+=1
        
print(c)
