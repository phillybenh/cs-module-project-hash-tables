data = [None] * 16 # Size should be a power of 2

def my_hash(s):
    """Beej's naive hashing function"""

    sb = s.encode()

    total = 0

    for b in sb:
        total += b
        # next lines force python to limit the range to 32 or 64 bit
        total &= 0xffffffff # add this for a 32-bit hashing fcn
        #total &= 0xffffffffffffffff  # add this for a 64-bit hashing fcn
    return total

def get_index(s):
    h = my_hash(s)

    i = h % len(data)

    return i

def put(k, v):
    # Get the index into "data" to store "v"
    i = get_index(k)

    # Store v there
    data[i] = v

def get(k):
    i = get_index(k)

    return data[i]

def delete(k):
    i = get_index(k)

    v = data[i]

    data[i] = None

    return(v)


put("beej", 3490)
put("goats", 999)
put("beej", 111)

print(data)

print(get("goats"))

# print(my_hash("ben"))
# print(my_hash("benjamin"))

# print(get_index("ben"))
# print(get_index("benjamin"))


