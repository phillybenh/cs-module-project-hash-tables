# Indexing
#
# What are all the employees in a certain department?

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]
# build index lookup table O(n)
# then each lookup will be O(1)
index = {}

def build_index():
    for r in records:
        dept = r[1]

        if dept not in index:
            index[dept] = []
        
        index[dept].append(r)

build_index()

while True:
    dept = input("Enter department: ")
    print(index[dept])



"""
# O(n) soliution is to loop thru everything
for r in records:
    if r[1] == dept:
        print(r)
"""