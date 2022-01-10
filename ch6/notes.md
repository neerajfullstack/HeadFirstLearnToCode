# Putting it all togather

 Let's grab some text, slice it, dice it, and then do a little data analysis on it. We are going to find out what a heruistic too, and implement one.


 Here's is what you need to do:

 Examine:
    - every sentence
    - every word
    - every syllable
not to mention every single character of the text in question!


# The game plan:

1. To compute the total number of words in our text: that means we'll have to take each word, figure out how many syllables it has, and then add up all the syllables in the entire text. 



# High Level Psuedocode

Define a function computer_readability(text):
    var total_words = 0
    var total_sentences = 0
    var total_syllable = 0
    var total_score = 0

    total_words = count_words(text)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text)

    score = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)

    IF score >= 90.0:
        PRINT ‘Reading level of 5th Grade’
    ELIF scores >= 80.0:
        PRINT ‘Reading level of 6th Grade’
    ELIF scores >= 70.0:
        PRINT ‘Reading level of 7th Grade’
    ELIF scores >= 60.0:
        PRINT ‘Reading level of 8-9th Grade’
    ELIF scores >= 50.0:
        PRINT ‘Reading level of 10-12th Grade’
    ELIF scores >= 30.0:
        PRINT ‘Reading level of College Student’
    ELSE:
        PRINT ‘Reading level of College Graduate’



# We need some text to analyze

Before we get coding, we're going to need some interesting text to put through our analysis. Now the truth is, you can analyze any text you want: blog posts, your own writing, new articles, books - whatever - and half the fun of creating this code is analyzing your new outlets and writers. That said, as we build and test this code, it'll help if you use the same text we use, so we're seeing the same results. So let's find some text we can all test togather. 

And why not put ourselves to the rest? We're going to use the first couple of pages of this book, which you'll find the file in ch6/text.txt



# How to get multiline text into Python

if you look at the file ch6/text.txt, you'll see we have a big text file, but how do we get that into Python? Well, you already know how to add text to your code with string:

We are going to use a python convetion for entering strings that span multiple lines by using triple quotes, like this:



text = """The first thing that stands between you and writing your first, real,piece of code, is learning the skill of breaking problems down into acheive little actions that a computer can do for you."""





