n=int(input("enter n : "))
sum=0
for i in range(n):
    if i%2 !=0:
        sum+=1
        print(i,end=' ')

print("\nThe sum of odd numbers : ",sum)


