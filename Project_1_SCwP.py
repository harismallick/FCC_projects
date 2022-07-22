# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:37:47 2022

@author: Haris.Mallick
"""

import re
import operator

# test = '9999'
# op = '+'
# print(op + test)

def arithmetic_arranger(arr, show_ans=False):
    
    if len(arr) > 5:
        
        return print('Error: Too many problems.')
    
    operand_list = []
    operator_list = []
    
    for item in arr:
        
        # Error handling clauses
        
        letter_search = re.findall('[a-zA-Z]', item)
        
        if letter_search != []:
            return print('Error: Numbers must only contain digits.')
        
        mul_div_search = re.findall('[\*\/]', item)
        
        if mul_div_search != []:
            return print('Error: Operator must be \'+\' or \'-\'.')
        
        split = re.split('[\+\-]', item)
        #print(split)
        split[0] = split[0].strip()
        split[1] = split[1].strip()
        #print(split)
        
        for num_str in split:

            if len(num_str) > 4:
                return print('Error: Numbers cannot be more than four digits.')
        
        if '+' in item:
            operator_list.append('+')
            
        else:
            operator_list.append('-')
        
        size_diff = len(split[0]) - len(split[1])
        
        if size_diff > 0:
            temp = split[1]
            split[1] = ' '*size_diff + temp
            
        else:
            temp = split[0]
            split[0] = ' '*(-1*size_diff) + temp
        
        operand_list.append(split)
        
    #print(operand_list)

    # Go to separate function to perform the arithmetic operation.
    # Operation results will be stored in a separate list.

    answers, top_line, bot_line = arithmetic(operand_list, operator_list)
    
    # Now print the different elements in the desired order:
        
    #print(top_line)
    #print(bot_line)  
    
    for num in top_line:
        print(num, end='\t')
        
    print('\n', end='')
    
    for num in bot_line:
        print(num, end='\t')
        
    print('\n', end='')
    
    # Printing the dashed line:
    
    dash = '-'
    #dashes = [dash] * len(operand_list)
    
    for num in bot_line:
        dashes = dash * len(num)
        print(dashes, end='\t',)
        #print(dash, end='')
        
    print('\n', end='')

    if show_ans:
        for answer, line in zip(answers, bot_line):
            front_spacing = len(line) - len(answer)
            space = front_spacing*' '
            print(f'{space}{answer}', end='\t')
    
        
def arithmetic(num_arr, op_arr):
    
    operators = {
        '+': operator.add,
        '-': operator.sub
    }
    answers = []
    top_line = []
    bot_line = []

    for nums, op in zip(num_arr, op_arr):
        operation = operators[op](int(nums[0]), int(nums[1]))
        answers.append(str(operation))
        
        top_line.append('  ' + nums[0])
        bot_line.append(op + ' ' + nums[1])

    #print(answers)

    return answers, top_line, bot_line
        
        
def main():
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
    
if __name__ == '__main__':
    main()