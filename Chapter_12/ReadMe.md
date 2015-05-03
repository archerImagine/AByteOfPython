# Chapter 12 | Object Oriented Programming #

## Introduction ##

We have written a lot of code till now, these codes were mostly data manipulation code, where every thing happened sequentially and by calling different functions from one or many function, this type of programming is called **Procedural Programming.**

There is another type of programming were we combine the data and the functionality into a single entity which we call as Class. This programming idea is called **Object Oriented Programming.**

There are two main aspect of **Object Oriented Programming**:

* **Class** : A **Class** creates new type.
* **Objects** : A **Objects** is **instances** of the class.

Two main components are involved in a Objects, which is a instance of a Class.

* **Fields**:- Variables which belongs to a class or object where we store data are called **Fields**. These are of two types.
    - **Instance Variables** : Variables which belongs to a particular object instances.
    - **Class Variables** : Variables which are shared across all the object instances.
* **Methods**:- Object can also have functionality in addition to storing data, The functionality is provided by the function within a object which is called **Methods.**

TODO: One question which we have to find answer is to is there any class methods or static methods.

* [The definitive guide on how to use static, class or abstract methods in Python ](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)

## The `self` ##

Methods are nothing but function inside a class, but it has one major difference than any other normal function. In a method definition, the first argument is always `self `, similar to `this ` in Java or C++.

This first argument `self ` refers to the object itself and by convention it is called `self `, though we can name as anything but it is advisable to name it `self `.

One important question remains, i.e. **how does self gets its value?**

Consider this, we have a class called `MyClass` and an instance of this class called `myobject` . When we call a method on `myobject` instance, we call it using `myobject.method()`, this gets converted to `MyClass.method (myobject)`

## Classes ##
The most simplest class will be

````python
class Person(object):
    pass # Empty Block

p = Person()
print p
````

gives a output:-

````
<__main__.Person object at 0x10d455a10>
````

Few things to note in the above code:-

* Use the keyword `class` to create a class.
* Instance is create just by calling the class name, as shown by `p = Person()`

## Methods ##

Here is an example of Methods in action.

````python
class Person:
    def sayHi(self):
        print "Hello, How are you."

p = Person()
p.sayHi()
````



