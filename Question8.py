'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010'''

#Program

list1=input().split(',')
for x in list1:
    if(x%5)==0:
        print(x)
    else:
        print("No numbers are divisible by 5")
    
