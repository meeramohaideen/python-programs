n=int(input("Enter the size of an array"))
arr=[]
for i in range(0,n):
    v=int(input("Enter"))
    arr.append(v)
print(arr)
c=abs(arr[0]+arr[1])
print(c)
for i in range(0,n):
	for j in range(1,n):
		d=abs(arr[i]+arr[j])
		#print (d)
		if(d<c):
			c=d
			a=arr[i]
			b=arr[j]
print("%d and %d"%(a,b))			
