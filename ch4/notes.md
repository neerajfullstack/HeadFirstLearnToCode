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
