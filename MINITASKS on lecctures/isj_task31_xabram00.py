# minitask 3.1

mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
wanted = {'a': 17, 'b': 34, 'z': 3}
n_mcase = {}
for k,v in mcase.items():
    if k.lower() in n_mcase.keys():
            v=mcase[k]+n_mcase[k.lower()]
    n_mcase.update({k.lower():v})
