

from functools import cmp_to_key

class elevator:
    def __init__(self, kwargs):
        self.major = int(kwargs['major'])
        self.minor = None
        self.revision = None
        self.index = kwargs['index']
        if 'minor' in kwargs:
            self.minor = int(kwargs['minor'])
        if 'revision' in kwargs:
            self.revision = int(kwargs['revision'])

    def __str__(self):
        return self.major+'.'+self.minor+'.'+self.revision



l = [str(x) for x in raw_input().strip().split()]
arr = []
i =0
for elev in l:
    elev = elev.split('.')
    kwargs = {}
    kwargs['major'] = elev[0]
    kwargs['index'] = i
    if len(elev)>1:
        kwargs['minor'] = elev[1]
    if len(elev)>2:
        kwargs['revision'] = elev[2]
    arr.append(elevator(kwargs))
    i+=1

def compare(a,b):
    if a.major>b.major:
        return 1
    if a.major<b.major:
        return -1
    if a.minor is None and b.minor is not None:
        return -1
    if a.minor is not None and b.minor is None:
        return 1
    if a.minor<b.minor:
        return -1
    if a.minor>b.minor:
        return 1
    if a.revision is not None and b.revision is None:
        return 1
    if a.revision is None and b.revision is not None:
        return -1
    if a.revision<b.revision:
        return -1
    if a.revision>b.revision:
        return 1

cmp_items = cmp_to_key(compare)
arr.sort(key=cmp_items)
res = [l[a.index] for a in arr]
print(res)


