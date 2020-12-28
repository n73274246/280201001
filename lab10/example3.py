def sum_of_nested(x):
 if not isinstance(x,list):
    return x
 else:
   sum_result = 0
   for item in x:
     sum_result += sum_of_nested(item)
   return sum_result

a_list = [3,12,76,[4,56,43],[2,8],81,75]
print(sum_of_nested(a_list))
