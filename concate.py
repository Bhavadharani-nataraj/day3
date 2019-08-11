d1={1:'a',2:'b'}
d2={3:'d',4:'e'}
d3={}
for d in (d1,d2):
    d3.update(d)
print(d3)
