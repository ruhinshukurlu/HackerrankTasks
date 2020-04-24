# Apple and Orange
# link : https://www.hackerrank.com/challenges/apple-and-orange/problem

def add_list(arr,a):
    new_list = []
    for b in arr:
        new_list.append(int(b) + a)
    return new_list


start, end = map(int, input().split())
apple, orange = map(int, input().split())

apple_count, orange_count = map(int, input().split())

apple_list = input().split(' ')
orange_list = input().split(' ')


new_apple_list = add_list(apple_list, apple)
new_orange_list = add_list(orange_list, orange)

c_1 = 0
c_2 = 0

for a in new_apple_list:
    if a >= start and a <= end:
        c_1 +=1

for b in new_orange_list:
    if b >= start and b <= end:
        c_2 +=1

print(c_1)
print(c_2)