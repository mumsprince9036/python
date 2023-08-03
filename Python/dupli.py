print("Enter Array Elements:")     
l=list(map(int,input().split()))
l=set(l)
l=list(l)
for i in range(len(l)):
    print(l[i],end=" ")
