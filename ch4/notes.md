# The for loop, the prefered way to iterate over a list

You can use while loop to iterate over lists, but recommended way is for loop. You should use while loop when you want to do something while something true or false. 

Use for loop when you need to iterate over a sequence. 

# How the for loop works on a range of numbers

There's another kind of sequence the for loop works on: a range of numbers. Python has a built in function called range that you can use to generate different sequences of numbers. After you've generated a sequence of numbers, you can use the for loop to iterate through them. 

range(5)

for i in range(5):
    print('iterating through', i)

length = len(smoothie)

for i in range(length):
    print('Smoothie #', i, smoothies[i])


# Doing more with ranges:

With a range you don't have to create sequences from zero to some number, you can create all kinds of ranges of numbers. 

Try a starting and ending number

range(5,10)


Key bits:

When you use while loop, you need to initialize your counter increment in separate statements. If, after lots of code changes, you accidently moved or deleted one of these statements, well then things could get ugly. But with a for loop, everything is packaged right in the for statement for all to see and with no chance of things getting changed or lost.

# Bullet Points

- Lists are a data structures for ordered data.
- A list holds a set of items, each with its own index
- List uses a zero-based index, where the first item is index 0
- You can access any item using its index. For example, use my_list[1] to access the second item in the list
- You can also use negative indices to identify items at the end of list
- Trying to access an item beyond the end of list will result in a runtime index error
- Assigning a value to an existing item will change its value
- Assigning a value to an item that doesnt exist in the list result "out of bounds" runtime error.
- List items can hold values of type
- Not all the values in a list need to be same type
- List that hold values of different types are called heterogeneous
- You can create an empty lists with my_list = []
- You can add a new value to a list using append.
- You can add a new value to a list append
- You can extend a list with the items in another list with extend
- You can create a new list from two exising by simply adding them togather +
- Use insert to add a new item at an index in an exising list


# Getting Functional 

