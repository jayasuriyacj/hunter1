inp1=int(input())
inp2=1
while(inp2<=inp1 and inp2*2<=inp1):
    inp2=inp2*2
if(inp2==inp1):
    print("0")
else:    
    print(inp1-inp2)
