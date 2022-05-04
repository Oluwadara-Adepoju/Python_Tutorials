
"""
This is a multiplication table which allows the user to input a number 
and the algorithm outputs a multiplcation table
"""
from distutils.log import error


num = int(input('Enter a number: '))
int_num = 0
while int_num <=12:
    ans = num* int_num
    print(' {}   +  {} =  {} '.format(num,int_num,ans))
    int_num = int_num + 1

    match error:
        case ValueError:
            print('Error must try again ')
