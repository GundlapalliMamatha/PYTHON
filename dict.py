d1={}
print(d1,type(d1))
l1=[10,20,30,40,50]
print(l1[0])
print(l1[4])
d2={}
d2[0]=10
d2[1]=20
d2['name']="mamatha"
print(d2)
d3={0:10,1:20,'name':'mamatha'}
print(d3[0],d3[1],d3['name'])
d4={0:10,1:20}
print(d3.keys()) #dict_keys([0, 1, 'name'])
print(d3.values()) #dict_values([10, 20, 'mamatha'])
print(d3.items()) # dict_items([(0, 10), (1, 20), ('name', 'mamatha')])