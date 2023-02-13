li=[]
n= int(input("Enter the number of elements "))
for i in range (0,n):
    ele=int(input())
    li.append(ele)
    
s=set(li)
for i in s:
    flag=0
    for j in li :
        #print(i,j,end=" ")
        print()
        if(i==j):
            flag=flag+1;
        else:
            pass
        
    if(flag==1):
        print(i)
        break