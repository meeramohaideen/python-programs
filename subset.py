n=int(input("Enter the size of an array"))
k=int(input("Enter the size of an array1"))
arr=[]
arr1=[]
for i in range(0,n):
    v=int(input("Enter"))
    arr.append(v)
print(arr)
for i in range(0,k):
    v=int(input("Enter"))
    arr1.append(v)
print(arr1)
c=0
for i in range(0,n):
	for j in range(0,k):
		if(arr[i]==arr1[j]):
			c=c+1
print(c)			
if(c==n):
	print("arr is the subset of arr1")
else:
	print("arr is not the subset of arr1")
