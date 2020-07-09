# Hash Tables

 - a *hash function*  is a function where the input is any data, and the output is a number
 - Requirements of a hash function:
     - A hash function must be consistent (deterministic). Every time it receives the same input (like "aqua"), it must return the same output (like 4). If it’s not deterministic, it is not a hash function
     - Different input data should return different numbers. For example, if the input "aqua" returns 4, then the input "beige" should not return 4
         - The reason the hash function should return different numbers when given different input data is to minimize collisions
     - A hash function must return numbers that are within a specific range

## Day 1 Lecure Notes
 - work with bytes
 - use `.encode()` to convert strings to bytes

 ### Hash Tables in particular languages
 - Python: dict
 - JavaScript: object (sometimes), Map
 - Swift:  Dictionart, Hashtable, Hashmap

## Day 2 Lecure Notes
Slot
Index Chain (linked list)
----- -------------------------------
 0    -> ("qux",10) -> None
 1    -> ("plugh",20) -> ("foo",55) -> None
 2    -> ("xyzzy",50) -> ("baz",999) -> ("bar",30) -> None
 3    -> None

put("foo", 12)
put("bar", 30)
put("baz", 999)
put("qux", 10)
put("plugh", 20)
put("xyzzy", 50)
put("foo", 55)

get("baz")


Hash function results
---------------------
"foo" -> 1
"bar" -> 2
"baz" -> 2 -- collision!
"qux" -> 0
"plugh" -> 1 -- collision!
"xyzzy" -> 2 -- collision!


Pseudocode for put
------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Overwrite the value
* Else it doesn't exist:
  * Make a new record (`HashTableEntry` class) with the key and value
  * Insert it anywhere in the list

Pseudocode for get
------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Return the value
* Else it doesn't exist:
  * Return `None`

Pseudocode for delete
---------------------
* Find the index in the hash table for the key
* Search the list at that index for the key
* If it exists:
  * Delete the entry from the linked list
  * Politely return the deleted value
* Else it doesn't exist:
  * Return `None`

Linked list node
----------------

class HashTableEntry:   # Node in the linked list
    def __init__(self, key, value):
	    self.key = key
        self.value = value
        self.next = None   # Make this a linked list node

Load Factor
-----------

The number of records in the hash table vs. the number of slots in the array


data = [None] * 32

put("1",99)
put("2",99)
put("3",99)
put("4",99)
put("5",99)
put("6",99)
put("7",99)
put("8",99)
put("9",99)
put("10",99)
put("11",99)
put("12",99)

load factor = 12 / 32 = 0.375

If the load is 1.0, we exactly the name number of data elements as array elements.

Resizing a hash table
---------------------

If the load > 0.7: resize

Resize:

* Make a new array with _double_ the capacity of the old one
* Have the hash table refer to that new array
* Run through all the nodes in the old hash table array
  * Put them in the new hash table array

## Day 3 Lecure Notes

 - Applications of hash tables
     - Lookups
         - a digital phone book (maps a person’s name to their phone number)
         - DNS resolution (maps a web address to an IP address
         - student records (a unique student id maps to student information)
         - library system (a book’s unique identifier maps to detailed book information)
     - Duplicate Prevention
         - storing users (prevents creating duplicate users or overwriting a user)
         - a voting system (one person, one vote)
     - Memoization, Caching



