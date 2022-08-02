# import numpy as np
# l1=[True,True,True]
# l2=[True,True,True]
# l3=[True,True,True]
# arrys=np.array(l1,l2,l3)
# print(arrys)

# #   49
# l2=[]
# for i in range(0,6):
#   n=int(input(f"Enter {i}: "))
#   l2.append(n)
#   a = np.array(l2) 
# ll=[]
# odds= (a%2 == 1) 
# a[odds] = -1 
# ll.append(a)
# res=np.array(ll)
 
# print(res)

l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
ll=[]
for i in l1:
  for j in l2:
    if i==j:
      ll.append(i)
print(ll)