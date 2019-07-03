inp1=int(input())
inp2=[int(x) for x in input().split()]
inp3=[]
for i in range(0,len(inp2)):
        y=inp2[i:]
        z=max(y)
        if inp2[i]==z:
                inp3.append(inp2[i])
print(*inp3)
print(max(inp2))
