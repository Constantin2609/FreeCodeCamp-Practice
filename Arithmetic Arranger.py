# -*- coding: utf-8 -*-

# Created on Tue March 7 13:00:00 2023

# @author: User




            
#______________________________________________________________________________
#   A R I T H M E T I C  A R R A N G E R
#------------------------------------------------------------------------------

import re


def arithmetic_arranger(A, disp=False):
# Assigning some lists, needed toward the end of the code:    
    l1 = []
    l2 = []
    l4 = []
    l1Fin = []
    l2Fin = []
    l3Fin = []
    l4Fin = [] 
    max1l = []
    offs = []
    LTot = []
    
    if len(A) > 5:
        print('Error: Too many problems.')
    for i in range(len(A)):
        if '*' in A[i] or '/' in A[i]:
            print('Error: Operator must be \'+\' or \'-\'.')
            break
        elif not re.search('^[0-9]+[+\-*/][0-9]+$', A[i].replace(" ", "")):
            print('Error: Numbers must only contain digits.')
            break
# Extracting the part of a problem, that's to the left from the operator (part1), 
# then converting it into a string (p1st) through .join() method, and then 
# converting the latter into an integer (p1int):
        part1 = re.findall('^([0-9]+)[+\-*/]', A[i].replace(" ",""))
        p1st = ''.join(part1)
        p1int = int(p1st)
# The above comment, applied to the part to the right from the operator:
        part2 = re.findall('[+\-*/]([0-9]+)$', A[i].replace(" ",""))
        p2st = ''.join(part2)
        p2int = int(p2st)
# Extracting the operator and then converting it into a string through
# the .join method:
        sign = re.findall('([+\-])', A[i])
        signSt = ''.join(sign)
# Obvious enough:        
        if len(p1st) > 4 or len(p2st) > 4 :
            print ('Error: Numbers cannot be more than four digits.')
            break
        else:
# Counting the answers:
            if '+' in A[i]:
                ans = p1int + p2int
            if '-' in A[i]:
                ans = p1int - p2int
# Forming the lines of the output column of problems from top to bottom:            
            l1.append(f'{p1int:}')    
            l2.append(f'{p2int:}')
            l4.append(f'{ans:}')
# Finding max length of the first two lines of the output column of problems
# operator omitted:                                     
            max1l.append(max([len(l1[i]),len(l2[i])]))
            #maxl [i] = max([len(l1pure[i]),len(l2pure[i])])
            
# Appending the offsets (offs[i])  between the operator and the second operand (l2[i])
# to the offset list (offs):            
            offs.append(max1l[i]-len(l2[i])+1)
# Constructing PRELIMINARYLY second lines (for each problem column) by concatenating the operator, 
# whitespaces multiplied by the corresponding offset number offs[i],
# and the second operator (type = list):            
            l2[i] = signSt + ' '*offs[i] + l2[i]
# Appending the maximal width (which is equal to the overall length of a second 
# line, including the operator sign, + the gap between the columns) of every column
# to the list (lenTot) of maximal widths of every column:           
            LTot.append(len(l2[i])+4)
# Constructing full lines (type = list):           
            l1Fin.append(' '*(LTot[i]- len(l1[i])) + l1[i])
            l2Fin.append(' '*(LTot[i]- len(l2[i])) + l2[i])
            l3Fin.append(' '*4 + '-'*(LTot[i]-4))
            l4Fin.append(' '*(LTot[i]- len(l4[i])) + l4[i])
# Converting full lines from lists into strings:              
            L1 = ''.join(l1Fin)
            L2 = ''.join(l2Fin)
            L3 = ''.join(l3Fin)
            L4 = ''.join(l4Fin)
# Defining, whether to show the answer lines or not:          
            if disp :
                Columns = '\n' + L1 + '\n' + L2 + '\n' + L3 + '\n' + L4
            else:
                Columns = '\n' + L1 + '\n' + L2 + '\n' + L3 
            
    return Columns

   

print (arithmetic_arranger(["32 + 234", "1 + 380", "9 + 90", "5 - 2849", "5 - 4"], True))

print (arithmetic_arranger(["32 + 234", "1 + 380", "9 + 90", "5 - 2849", "5 - 4"], False))

print (arithmetic_arranger(["32 + 234", "1 + 380", "9 + 90", "5 - 2849", "5 - 4"]))
































