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