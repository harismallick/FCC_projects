# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 17:37:47 2022

@author: Haris.Mallick
"""

import re

test = '255*300'

# x = re.findall('[\*\/]', test)
# print(x)

# y = re.split('[\*\/]', test)
# print(y)

# test2 = ['15', '   16', '20' '\n15', '+ 161', '20']
# for item in test2:
#     print(item, end='    ')
#print(test2)

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
            if len(num_str) > 4:
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
        
    print(op_list)
        
        
        
        
        
def main():
    arithmetic_arranger(['2555+30', '25-3000'])
    
if __name__ == '__main__':
    main()