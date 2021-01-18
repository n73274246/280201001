def binarySearch(a_list,item):
  if len(a_list) == 0:
    return -1
  else:
    mid = len(a_list)//2
    if a_list[mid] == item:
      return mid
    elif item < a_list[mid]:
      index = binarySearch(a_list[:mid],item)
      return index
    elif item> a_list[mid]:
      index = binarySearch(a_list[mid+1:],item)
      return index+mid+1

mylist=[8,12,22,27,38]
print(binarySearch(mylist,22))
