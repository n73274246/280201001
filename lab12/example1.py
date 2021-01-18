
def selection_sort(x):
 n = len(x)
 for l in range(n-1):
   min_i = l
   for r in range(l+1,n):
     if x[min_i] > x[r]:
       min_i = r
   temp = x[l]
   x[l] = x[min_i]
   x[min_i] = temp
     

mylist = [22,8,12,-4,27,38,36,50,7,68,91,56,2,85,42,98,25]
selection_sort(mylist)
print(mylist)

