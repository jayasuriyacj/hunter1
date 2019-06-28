a1=int(input())
b1=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,a1):
    b1*=10
    b1+=int(array[a])
print(b1)
