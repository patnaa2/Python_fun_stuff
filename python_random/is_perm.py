#!/usr/bin/python

#use a a: [ c1, c2] structure

def is_perm(str1, str2):
    data = {}
    for c in str1:
        if c in data:
            data[c][0] += 1
        else:
            data[c] = [1]
    for c in str2:
        if c in data:
            try:                
                data[c][1] += 1
            except IndexError:
                data[c].append(1)
        else:
            data[c] = [0, 1]

    for list in data.values():
        try:
            if list[0] != list[1]:
                return False
        except IndexError:
            return False
    return True
        
print is_perm('stridsdfsng1', '1girnts')
