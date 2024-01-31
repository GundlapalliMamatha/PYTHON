def d1():
  print("d1 f")
  def d2():
   print("d2 f")
   
  return d2
   
d=d1()
print(d)
print(d.__name__)
   
   
   
