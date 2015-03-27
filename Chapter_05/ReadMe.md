# Chapter 05 | Basics #

## Comments ##

Comments are any text to the right of `#`. Few examples of comments are as below,

````
print "Hello World!"    #prints hello world.

#Print is a statement.
print "Hello World!"
````

Comments are necessary for coding because always remember, human memory is a bitch, so always comment your code, at least to find why you wrote the code.

Few important points which a comment can address:-

* explain assumptions.
* explain important decisions.
* explain important details.
* explain problem's you are trying to solve.

Always remember [Code Tells You How, Comments Tell You Why ](http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)

## Literal Constants ##

These are some of literal constants, `5`,`1.23`,`This is a string.` These are called literals because, its value is used literally as number `2` always represents itself, i.e. it is a constant as the value does not change.

## Numbers ##

Python has two types of **Numbers**

1. **integers**
2. **floats**.

### Integers ###
The example of Integers are whole numbers like `2`.

### Floats ###
The floating numbers are number with decimal points, example like `1.25` and `24.3 E -4`

The `E` notation indicates power of `10`

> There is no long type in python.

## Strings ##

A string is a sequence of character within one of these type of quotes.

* Single Quotes `' '`
* Double Quotes `" "`
* Triple Quotes `""" """`

Here is an example of strings, `"This is a string"`

We can use the above 3 Quotes to specify string.

* Single Quotes `'This is Single Quote String'`
* Double Quotes `"This is Double Quote String"`
* Triple Quotes `"""This is Triple Quote String"""`
    - Triple Quotes can be uses to specify multi line strings.
    - You can also use `''' '''`, to specify triple quotes.

### String Mutability ###

Strings are Immutable, which means, once created we cannot change a string.

> There is no `char` type in Python.

### `format()` method ###

`format()` method help us to create a string from various other information.

````
age = 20
name = "Archer"

print '{0} was {1} years old, when he learned Python.'.format(name,age)
print 'why is {0} learning Python?'.format(name)
````
The piece of code like `{0}` and `{1}` are nothing but just similar to fill in the blanks type of question in our class exams, where the value is filled by the `.format()` arguments, `name` fills the blank at `{0}` and `age` fills the blank at `{1}`

> The numbers inside `{}` are optional.

More formally, python in the `format()` method substitute each argument value into the specification.

### Escape Sequence. ###


## Variable ##
## Identifier Naming ##
## Data Type ##
## Object ##
## Logical and Physical Line ##
## Indentation ##
