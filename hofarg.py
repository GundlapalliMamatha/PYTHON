def d1(para1,para2):
    
    return "para1",para1,para2
def d2():
    return "para2"

def d3():
    return "para3"

d=d1(d2(),d3())
print(d)
