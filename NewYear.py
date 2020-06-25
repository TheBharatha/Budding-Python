n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for elem in array:
    happiness += elem in a
    happiness -= elem in b
print(happiness)