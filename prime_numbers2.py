n=int(input("Please enter prime numbers limit(1-n): "))
prime_list=[]
for i in range(2,n+1):
    count = 0
    for j in range(1, i+1):
        if not i % j:
            count +=1
    if (i==0) or (i==1) or (count>=3):  
        continue
    else:
        prime_list.append(j)
print(prime_list)