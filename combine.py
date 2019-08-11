d1={'a':1,'b':2}
d2={'c':3,'b':4}
for key in d2:
    if key in d1:
        d2[key]=d2[key]+d1[key]
    else:
        pass
print(d2)
