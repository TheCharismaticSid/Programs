'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.'''

words = input().split()  #takes input and accepts whitespace by using split
for a in words:               #loop to check the words
    if words.count(a)>1:   #checks each word and if same word is found more than once removes it
        words.remove(a)
words.sort()  #sorts 
print(" ".join(words))  #used join to remove this "[" and this ","  from the output
