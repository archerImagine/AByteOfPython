# Chapter 09 | Modules #

## Introduction ##

We all know that we should always reuse code, the few ways of doing it are:-

* by writing reusable function.
* To have a module with resuable function.
* write the module in native language, and provide a python interface.

We will discuss in details the 2nd option which we have. To create modules the most simplest way is to create a `.py` file with functions in it.

This module which we created can be `import`**ed**, by another program to make use of these function.

The most simplest use of module can be understood by importing the `sys` module.

````
import sys

print ("the Command line arguments are: ")

for i in sys.argv:
    print i

print "\n\nThe PYTHONPATH is", sys.path,"\n"
````

Lets dissect the above code:-

* `import sys` : This tells python, that we want to use the functionality of this module called `sys`. 
    - Since `sys` is a built in module, the python interpreter knows where to find this module.
    - If it was not a standard module, it will search in `sys.path` directories.
    - Initialization is only done at the time of `import`
* `sys.argv` : This is a list of strings, which contains the command line arguments passed to the program.
    - The name of the script is always the first element of `sys.argv`
* `sys.path` : This contains the list of directory from which we can import modules.
    - The first output of the above is the current directory.

## Byte-compiled .pyc files ##

## The `from ... import ` statement ##

## A module's name ##

## Making your own modules ##

## The `dir` function ##

## Packages. ##