
# we use yield to create a list, this list is created as we need it:

def getpairs (limit):
    n =1
    while n< limit:
        yield n *2
        n = n +1
      
        

for i in getpairs(10):
    print (i)