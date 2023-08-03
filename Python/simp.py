num=int(input("enter any number "))
high = int(input("enter the upper rangs"))
power = len(str(num))

sum = 0
temp = num
while temp>0:
    rem = temp%10
    sum=sum+rem**power
    temp//=10
if num == sum:
    print("is an armstrong ")    
else:
    print("its not")    