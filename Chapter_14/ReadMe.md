# Chapter 14 | Exceptions #

**Exceptions** occurs due to exceptional situation occurs in the program, which is very rare to happen. When such situation happens Python **raises** its hands to tell about the **error**.

## Errors ##

What will be the error in this line of code

````python
Print "Hello World!"
````

It gives the error

````python
File "example01.py", line 1
    Print "Hello World"
                      ^
SyntaxError: invalid syntax
````

As you can see a `SyntaxError` is raised.

## Exceptions ##

Consider the below code:-

````python
s = raw_input("Enter Something -----> ")
````

When the console is waiting to receive keys, press `Ctril + D`, we will get a `EOFError` which is really an exceptional situation.

## Handling Exceptions ##

We can handle exception using `try ... except ` statement.

Put the normal statement inside the `try` block and all error handlers in `except ` block.

Consider this code:-

````python
try:
    text = raw_input("Enter Something ---> ")
except EOFError:
    print "Why did you do an EOF on me?"
except KeyboardInterrupt:
    print "You cancelled the operation"
else:
    print "you entered {}".format(text)
````

What we are doing in the above code is:-
* Putting all the error prone code, in the `try` block.
* Then have respective handlers for error which we are expecting in the `expect ` block.
    - If a `except ` block has no name exception, it will handle all error.
    - There should be atleast on `except ` block.
* If the program does not handle the errors, it will be done by python default handlers.
* The `else` clause is executed when not error occurs.