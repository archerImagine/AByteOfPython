# Chapter 10 | Data Structures #

# Introduction #
There are four built-in data structures in python.

1. list
2. tuple
3. dictionary
4. set

## List ##

A list holds a ordered collection of items.

Few important things about list:-

* List are mutable, i.e. the list members can be added, removed, or merged without creating a new list.
* List are denoted by `[]`
* Ordered collection, means the order items are put in the list it comes out in the same manner

One important thing not related to List, which is mentioned is,
````
print items,
````

The above line will print all the items in the same line instead of multiple lines.

All the modification methods on list like, `append()`, `sort()` all work on the same list, no temporary list is created.

## Tuple ##

Few things to remember about tuples.

* Tuple's are immutable, i.e., it cannot be modified, even if modified, it will create a new tuple.
* Tuple are denoted by `()`, which are optional

A tuple with just one element have a special syntax, `(8,)`
