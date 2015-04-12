# Chapter 08 | Functions #

## Introduction ##

Functions are reusable piece of code, The use of function is to give a name to a block of code. So this block of code can be executed multiple time when we invoke the function by using its name.

`len()` & `range()` are two function which we have already seen.

Here is a sample implementation of a function.

````
def sayHello():
    # Block belong to function
    print "Hello World"
# End of function
````
Few important things to remember from the above code:-

* Functions are defined using the keyword `def`
* The `def` keyword is followed by an identifier which is the function name.
* Identifier name is followed by pair of parentheses, which may include some variables names called parameters.
* Finally it has `:` to indicate the start of block
* Next is the block which is part of the Function.

## Functions Parameters ##

A Function can take parameters, which values are consumed by the function to produce some outputs. Parameters are similar to variables, just the only difference that Parameters can be never be without a initial value unlike variable.

Parameters are specified within the parentheses of the function definition separated by comma. When the function are invoked it has the arguments in the same order.

The names given in the function definition is called parameters, and the value we supply while calling are called arguments.

Here is an example of the both:-

````
def printMax(a,b):
    if a > b:
        print a, " is maximum. "
    elif a == b:
        print a, " is equal to ", b
    else:
        print b, "is maximum"

# Directly Pass the Literal Value

printMax(3,4)

x = 5
y = 7

# Pass the variable as arguments.
printMax(x,y)
````

## Local Variables ##

## The `global ` statement ##

## Default Argument Value ##

## Keyword Arguments ##

## VarArgs Arguments ##

## The `return ` statement ##

## DocString ##
