from pkg_resources import WorkingSet


def getpairs (limit):
    it = 1

    while it < limit:
        yield it * 2
        it = it+1
        

working = getpairs(10)

for i in working:
    print (i)
