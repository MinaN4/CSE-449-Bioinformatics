#
#
#     Mina Nazieh Azer
# 
#

from typing import IO
import numpy as np
from tabulate import tabulate
# works only with two sequences of the same length
def createMatrix(m,l1,l2,s1,s2):
    m= [ [ 0 for i in range(l1+1) ] for j in range(l2+1) ]
    #intialze headers for columns
    for i in range(l1):
        m[0][i+1]= s1[i] 
    #intialize header for rows
    for i in range(l2):
        m[i+1][0]= s2[i]
    return m    
def print_null():
    for i in range(1,len2+1): #columns
        for j in range(1,len1+1):#rows
            if matrix1[i][j]==0:
               matrix1[i][j]=""   
    print (tabulate(matrix1,tablefmt="fancy_grid"))

print("")
print("")
print("Mina Nazieh Azer")
seq1 = list("ACCTTGTCCTCTTTGCCC") #rows
seq2 = list("ACGTTGACCTGTAACCTC") #columns
len1=len(seq1)
len2=len(seq2)
matrix1=0
matrix1= createMatrix(matrix1,len1,len2,seq1,seq2)
window_size=9
step=3 # incremnt by 4
threshold=4
print("sequence 1: ",*seq1)
print("sequence 2: ",*seq2)
print("")
print("Window size= ",window_size,"  step= ",step,"  threshold = ",threshold)
matches=0
align1=""
align2=""
align1=list(align1)
align2=list(align2)

def loop_match(starti,startj,a,b):
    num_match=0
    j=start_j
    align1=""
    align2=""
    align1=list(align1)
    align2=list(align2)
    for i in range(starti,b+1): #columns
        if(matrix1[i][0]==matrix1[0][j]=="A" ):
            num_match=num_match+1
            align1.insert(len(align1),"A" )
            align2.insert(len(align2),"A" )
        elif(matrix1[i][0]==matrix1[0][j]=="T" ):
            num_match=num_match+1
            align1.insert(len(align1),"T" )
            align2.insert(len(align2),"T" )
        elif(matrix1[i][0]==matrix1[0][j]=="C" ):
            num_match=num_match+1
            align1.insert(len(align1),"C" )
            align2.insert(len(align2),"C" )
        elif(matrix1[i][0]==matrix1[0][j]=="G" ):
            num_match=num_match+1
            align1.insert(len(align1),"G" )
            align2.insert(len(align2),"G" )
        else:
            align1.insert(len(align1),matrix1[i][0] )
            align2.insert(len(align2),matrix1[0][j] )    
        j=j+1  
    print("")    
    print("Alignment :",*align2)
    print("           ",*align1)   
    print("matching letters = ",num_match)
                
    if(num_match >= threshold):
        matrix1[start_i+int((b-start_i)/2)][start_j+int((a-start_j)/2)]="⦿" 
        print("Action => Plot a dot")
        print_null()
        return 0
    print("Action => no action")         
    return 0
i_range=0
j_range=0
test1=window_size
while(test1<len1+step+1):
    test1=test1+1+step
    i_range=i_range+1

test2=window_size
while(test2<len2+step+1):
    test2=test2+1+step
    j_range=j_range+1
start_i=1
start_j=1   
data=1 
while(step>=0 and data==1):
    for i in range(start_i,i_range+1): #columns
        for j in range(start_j,window_size+start_j-1):#rows
            loop_match(start_i,start_j,start_j+window_size-1,start_i+window_size-1)      
            if(start_i==start_j==len1-window_size+1):
                data=0
                break
            start_j=start_j+step 
            if start_j== len1-window_size+1+step:
                start_j=1
                break   
        if data==0:
            break       
        start_i=start_i+step
    if start_i==len1-window_size+1+step:
         start_i=1


print("Final matrix ")
print_null()         