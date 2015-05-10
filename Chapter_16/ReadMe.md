# Chapter 16 | More #

## Passing Tuple around ##

We might have thought of returning more than 1 values as a return type a lot of time, and most time we used array to return multiple values. We have an option of returning a tuple in python. Which can return atleast 2 values.

````python
def getErrorDetails():
    return (2,'details', "hello")

errNum, errStr, errStr2 = getErrorDetails() 

print "errNum: ", errNum
print "errStr: ", errStr
print "errStr2: ", errStr2
````

In the above example we are returning 3 values. The usage `a,b = <some expression >` interprets the result of the expression as a tuple of two values.

As are use case of tuple, the fastest way to swap two values is

````python
a,b = 10,12

a,b = b,a

print a,b
````