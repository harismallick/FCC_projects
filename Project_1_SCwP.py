# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:37:47 2022

@author: Haris.Mallick
"""

import re
import operator

def arithmetic_arranger(arr, show_ans=False):
    
    if len(arr) > 5:
        
        return print('Error: Too many problems.')
    
    op_list = []
    
    for item in arr:
        
        #print(item)
        
        letter_search = re.findall('[a-zA-Z]', item)
        
        if letter_search != []:
            return print('Error: Numbers must only contain digits.')
        
        mul_div_search = re.findall('[\*\/]', item)
        
        if mul_div_search != []:
            return print('Error: Operator must be \'+\' or \'-\'.')
        
        split = re.split('[\+\-]', item)
        
        for num_str in split:
            if len(num_str) > 5:
                return print('Error: Numbers cannot be more than four digits.')
        
        if '+' in item:
            split.insert(1, '+ ')
            
        else:
            split.insert(1, '- ')
        
        size_diff = len(split[0]) - len(split[-1])
        
        if size_diff > 0:
            temp = split[-1]
            split[-1] = ' '*size_diff + temp
            
        else:
            temp = split[0]
            split[0] = ' '*(-1*size_diff) + temp
        
        op_list.append(split)
        
    #print(op_list)

    # Go to separate function to perform the arithmetic operation.
    # Operation results will be stored in a separate list.

    answers = arithmetic(op_list)
    
    # Now print the different elements in the desired order:
        
    top_line = []
    bot_line = []
    
    for op in op_list:
        
        top_line.append('  ' + op[0] + '    ')
        bot_line.append((op[1] + op[-1] + '    '))
        
    #print(top_line)
    #print(bot_line)  
    
    for num in top_line:
        print(num, end='')
        
    print('\n', end='')
    
    for num in bot_line:
        print(num, end='')
        
    print('\n', end='')
    
    # Printing the dashed line:
    
    dash = '------    '
    dashes = [dash] * len(op_list)
    
    for dash in dashes:
        print(dash, end='')
        
    print('\n', end='')

    if show_ans:
        for answer in answers:
            front_spacing = 6 - len(answer)
            space = front_spacing*' '
            print(f'{space}{answer}    ', end='')
    
        
def arithmetic(op_arr):
    
    operators = {
        '+ ': operator.add,
        '- ': operator.sub
    }
    answers = []

    for op in op_arr:
        operation = operators[op[1]](int(op[0]), int(op[2]))
        answers.append(str(operation))

    print(answers)

    return answers 
        
        
def main():
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
    
if __name__ == '__main__':
    main()