names = dict((('Jon',15), ('Ned',45), ('Arya',9), ('Catelyn',44), ('Bran',10)))
for ages in names.keys():
  if names[ages] < 18:
    print(ages)
