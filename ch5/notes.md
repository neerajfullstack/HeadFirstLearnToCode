You already know a lot. Variable and data types and conditionals iteration - that's enough to write basically any program you'd ever want to. 



# No Dumb Questions

# Do I need to define my function before the code calls it? Or can I put my functions at the end of the file?

No

We recommend defining functions at the top of your file for better clarity and organization. 

# local variable

A variable that is declared inside a function or a code block is called a local variable. 

That means you can only refer to that variable inside the body of the code block it is declared in. 

# Scope

Scope is the extent to which your variables are visible. It is an area of the program where you can access a variable, to read or change its value. A global variable is visible everywhere. 

Having to much global variables is not considerd a good thing. 

- Global Variable: Visible anywhere in your program, there is an exception though
- Local variable : visible inside function or code block body where it is declared

- Parameter : only visible inside function body where it is declared



# Passing variables to functions 

When you are passing a var to a function, you are actually passing the value of that variable. Not the var itself. 


# Going further with parameters:
Default values and keywords

Earlier we said you need to be careful about your argument order: if you don't pass the correct arguments in the correct order, the all bets are off in terms of how a function is going to operate. If you've got a function that has speed and altitude parameters and you switch the order when you pass your arguments, watch out!

This applies to most programming langauges.

To alleviate his potential ordering problem, Python provides a flexible way.

With python you can set default values and keywords, whic allows you to pick and choose arguments in order you want them. You will find parameter keywords and default values used in many python modules. 

# How default parameter values work

Your function parameter can have default values. Let's use a simpler version of our greet function, without a global variable. 

```PYTHON
def greet(name, message='you rule!'):
    print('Hi', name+ '.', message)

