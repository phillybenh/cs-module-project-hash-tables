# delux model with cashing the for 1000 
# when class initialized
# but also computes and caches any other values
class NumReverser:
    def __init__(self):
        self.cache = {}

	    # Build a lookup table
        for i in range(1000):
	        self.cache[i] = self.num_reverse(i)

    def num_reverse(self, n):
        if n in self.cache:
	        print("Cache hit")
	        return self.cache[n]

        # print("Cache miss")
        n2 = list(str(n))
        n2.reverse()
        n2 = ''.join(n2)   
    
        self.cache[n] = int(n2)

        return self.cache[n]


nr = NumReverser()
print(nr.num_reverse(123))
print(nr.num_reverse(1234))
print(nr.num_reverse(1234)) # cache hit this time





# classic lookup table version
"""
cache ={}
def build_lookup_table():
    for i in range(1000):
        cache[i] = num_reverse(i)

def num_reverse(n):
    n = list(str(n))
    n.reverse()
    n = ''.join(n)
    return n

build_lookup_table()
print(num_reverse(123))
"""

"""
# an alternative method  you'd just compute 
# as needed and cache. kinda depends what you 
# need for performance
def num_reverse(n):
    if n in cache:
	    return cache[n]

    n2 = list(str(n))
    n2.reverse()
    n2 = ''.join(n2)

    cache[n] = int(n2)

    return cache[n]
"""
