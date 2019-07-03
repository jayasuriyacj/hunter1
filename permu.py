from itertools import permutations
inp1=input()
inp2=permutations(inp1)
for j in list(inp2):
    print("".join(j))

