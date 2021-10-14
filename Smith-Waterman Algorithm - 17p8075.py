#    
#
#     j-1   |   j
#    |------|-----|
# i-1|   a  |  b  |
#    |------|-----|
#  i |   c  |  X  |
#    |------|-----|
#
#     X[j][i]
#     a[j-1][i-1]
#     b[j][i-1]
#     c[j-1][i]
#
#
#     Mina Nazieh Azer
# 
#

import numpy as np
from tabulate import tabulate


def createMatrix(m,l1,l2,s1,s2):
    m= [ [ 0 for i in range(l1+1) ] for j in range(l2+1) ]
  
    #intialze headers for columns
    for i in range(l1):
        m[0][i+1]= s1[i] 
    #intialize header for rows
    for j in range(l2):
        m[j+1][0]= s2[j]
    return m    



def maxm(a,b,c,state_match):
      
    if a>=b and a>=c:
        if state_match==1:
            a=a+match
            b=b+gap
            if b<0:b=0
            c=c+gap
            if c<0:c=0
        else:
             a=a+mismatch
             b=b+gap
             if b<0:b=0
             c=c+gap
             if c<0:c=0  
        if a<0:
            a=0
            max=0
        else:      
            max=a
          #add match or mismatch
    elif b>c and (c<=a or c>=a): #elif b>c and c<=a :
        b=b+gap
        c=c+gap
        if c<0:c=0
        if state_match==1:a=a+match
        else: a=a+mismatch
        if b<0:
            b=0
            max=0
        else:      
            max=b
    else:
        c=c+gap
        b=b+gap
        if state_match==1:a=a+match
        else: a=a+mismatch
        if c<0:
            c=0
            max=0
        else:      
            max=c


###################
    if a>=b and a>=c:
        return a
    elif b>c and (c<=a or c>=a):
        return b
    else:
        return c
        
    
match=5
mismatch=-2
gap=-6
state_match=0
statevalue=0
max=0         

#print('Enter first sequence:')
#seq1 = input()
#print('Enter second sequence:')
#seq2 = input()
seq1 = list("TGCTCGTA") #rows
seq2 = list("TTCATA") #columns
seq1=list(seq1) #rows
seq2=list(seq2) #columns

print("")
print("")
print("Mina Nazieh Azer")
print("sequence 1: ",*seq1)
print("sequence 2: ",*seq2)
print("match= ",match,"  mismatch= ",mismatch,"  gap= ",gap)

seq1.insert(0, 0)
seq2.insert(0, 0)

len1=len(seq1) 
len2=len(seq2) 

matrix1=0
matrix1= createMatrix(matrix1,len1,len2,seq1,seq2)

############## alignment matrix
matrix2=0
matrix2= createMatrix(matrix2,len1,len2,seq1,seq2)



state =0
for i in range(1,len2+1): #columns
    print("setp =>",i)
    print()
    matrix1[1][1]=0
    print (tabulate(matrix1,tablefmt="fancy_grid"))
    print()
    for j in range(1,len1+1):#rows
        
        a=matrix1[i-1][j-1]
        b=matrix1[i-1][j]
        c=matrix1[i][j-1]
        if(a=="i" or a=="j" or a=="A" or a=="C" or a=="T" or a=="G"):
             a=0
        if(b== "i" or b=="j" or b=="A" or b=="C" or b=="T" or b=="G"):
             b=0
        if(c== "i" or c=="j" or c=="A" or c=="C" or c=="T" or c=="G"):
             c=0
        
        if( matrix1[i][0] ==  matrix1[0][j]):
            state = 1 #match
        
        else: 
            state = 0 #mismatch
        
        matrix1[i][j] = maxm(a,b,c,state)
        
        
print("Step => last")
print()
matrix1[0][0]=0
print (tabulate(matrix1,tablefmt="fancy_grid"))
print()




####trace back to find haighest score position





def get_highest(mat,i,j):
    maxv=0
    im=0
    jm=0
    a=mat[j-1][i-1] #a
    c=mat[j][i-1]   #b
    b=mat[j-1][i]   #c
    current=mat[j][i]
    while(1):
        if  current> maxv:
            if mat[j][i]< b:
                return i,j-1,b 
            if mat[j][i]< c:
                return i-1,j,c      
            maxv =mat[j][i]
            im=i
            jm=j
        if mat[j][i] ==0:
            #
            return i,j,maxv    
        i-=1
        j-=1
        break
    return im,jm,maxv     
    
#print(matrix1[4][6])    
max_i=0 #second m[][i]
max_j=0 #first m[j][]
maxvalue=0
max_i,max_j,maxvalue= get_highest(matrix1,len1,len2)
#print(max_i,max_j,maxvalue)

matrix5=0
matrix5= createMatrix(matrix5,max_i,max_j,seq1,seq2)
matrix5[max_j][max_i]=maxvalue

align1=""
align2=""
align1=list(align1)
align2=list(align2)


while(max_i !=0 or max_j !=0):
    max_i,max_j,maxvalue= get_highest(matrix1,max_i,max_j)
    matrix5[max_j][max_i]=maxvalue
    if maxvalue !=0:
        align1.insert(0,matrix5[0][max_i] )
        align2.insert(0,matrix5[max_j][0] )
    if maxvalue==0:
        matrix5[max_j][max_i]=" 0"
        break
    #print(maxvalue)
    max_i =max_i-1
    max_j =max_j-1
    #print("")

for i in range(1,len2+1): #columns
    
    for j in range(1,len1+1):#rows
        try:
            if matrix5[i][j]==0:
               matrix5[i][j]=""
        except IndexError:
            break  
          
print("Alignment Matrix")
print

print (tabulate(matrix5,tablefmt="fancy_grid"))
print()

print("Alignment")
print(*align1)
print(*align2)

