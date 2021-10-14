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
match=2
mismatch=-1
gap=-1
state_match=mismatch
statevalue=0
allign="↖"
#"←↑↖"
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
    if(state_match==0):
        statevalue=mismatch
    else: 
        statevalue=match    
    max=0
    if a>=b and a>=c:
         max=a
          #add match or mismatch
    elif b>c and c<=a :
         max=b  #add gap penalty
    else:
         max=c  #add gap penalty
#### alignment #### #"←↑↖"
    global allign
    if(max==a and max==b and max !=c): allign="↖↑"
    elif(max==a and max==c) and max !=b: allign="←↖"
    elif(max==b and max==c and max !=a): allign="←↑"
    elif(max==a and max==b and max==c): allign="←↖↑"
    elif(max==a): allign="↖"
    elif(max==b): allign="↑"
    elif(max==c): allign="←"
    if max == a:
         return max+statevalue#+state    
    elif max == b:
         return max+gap
    elif max==c:
        return max+gap          

#print('Enter first sequence:')
#seq1 = input()
#print('Enter second sequence:')
#seq2 = input()

seq1 = list("ACGCTG") #rows
seq2 = list("CATGT") #columns
seq1=list(seq1) #rows
seq2=list(seq2) #columns

print("")
print("")
print("Mina Nazieh Azer")
print("sequence 1: ",*seq1)
print("sequence 2: ",*seq2)
print("match= ",match,"  mismatch= ",mismatch,"  gap= ",gap)


seq1.insert(0, "j")
seq2.insert(0, "i")

len1=len(seq1)
len2=len(seq2)

#### empty matrix for steps
matrix1=0
matrix1= createMatrix(matrix1,len1,len2,seq1,seq2)

############## dot matrix
matrix2=0
matrix2= createMatrix(matrix2,len1,len2,seq1,seq2)

### alignment matrix ###
matrix3=0
matrix3= createMatrix(matrix3,len1,len2,seq1,seq2)

###### final matrix with path
matrix4=0
matrix4= createMatrix(matrix4,len1,len2,seq1,seq2)
#####################


state =0
for i in range(1,len2+1): #columns
    print("setp =>",i)
    print()
    print (tabulate(matrix1,tablefmt="fancy_grid"))
    print()
    for j in range(1,len1+1):#rows
        #print(matrix1[i][j])
        a=matrix1[i-1][j-1]
        b=matrix1[i-1][j]
        c=matrix1[i][j-1]
        if(a=="i" or a=="j" or a=="A" or a=="C" or a=="T" or a=="G"):
             a=-100
        if(b== "i" or b=="j" or b=="A" or b=="C" or b=="T" or b=="G"):
             b=-100
        if(c== "i" or c=="j" or c=="A" or c=="C" or c=="T" or c=="G"):
             c=-100
        
        #if(matrix1[i][0]=="i"or matrix1[i][0]=="j" or  matrix1[0][j]=="i" or matrix1[0][j]=="j"): 
        if( matrix1[i][0] ==  matrix1[0][j]):
            state = 1 #match
        else: 
            state = 0 #mismatch
            #matrix2[i][j]= " "

        if(i==1 and j==1):
            matrix1[i][j]=0
            continue
        
        matrix1[i][j] = maxm(a,b,c,state)
        matrix3[i][j] = allign
        

print("setp =>","last")
print()
print (tabulate(matrix1,tablefmt="fancy_grid"))
print()

#print("Path-Matrix")
#print()
#print (tabulate(matrix3,tablefmt="fancy_grid"))
#print()

##### Needleman-Wunch Algorithm #####
for i in range(1,len(matrix1)):
   # iterate through columns
   for j in range(1,len(matrix1[0])):
       matrix4[i][j] = str(matrix3[i][j]) + str(matrix1[i][j])
print("Needleman-Wunch Algorithm")
print()
print (tabulate(matrix4,tablefmt="fancy_grid"))
print()

##### Tracing back
align1=""
align2=""
align1=list(align1)
align2=list(align2)

def traceb(mat,i,j,current):
    next=0
    a=matrix1[i-1][j-1] #a
    b=matrix1[i][j-1]   #b
    c=matrix1[i-1][j]   #c
    if(a=="i" or a=="j" or a=="A" or a=="C" or a=="T" or a=="G"):
             a=-100
    if(b== "i" or b=="j" or b=="A" or b=="C" or b=="T" or b=="G"):
             b=-100
    if(c== "i" or c=="j" or c=="A" or c=="C" or c=="T" or c=="G"):
             c=-100
    next=max(a,b,c)
    return next

#### traceback matrix
matrix5=0
matrix5= createMatrix(matrix5,len1,len2,seq1,seq2)
#####################


i=len2
j=len1
trace=matrix1[i][j]
current="x"
next=""
matrix5[i][j]=matrix1[i][j]
sym=["i","j","A","T","C","G"]
while(next != -100):
    
    #print(trace) #current value
    if i==j==1:break
    trace=traceb(matrix1,i,j,matrix1[i][j]) #next value
    if i== (j-1)==1:
        if (matrix1[0][j] in sym) == True:
            align2.insert(0,matrix1[0][j] )
            align1.insert(0,"-" )
        elif (matrix1[i][0] in sym) == True:
            align2.insert(0,"-" )
            align1.insert(0,matrix1[i][0])
        else:   
            align1.insert(0,matrix1[i][0] )
            align2.insert(0,matrix1[0][j] )      
        break
    if trace== matrix1[i-1][j-1]: #a
        align1.insert(0,matrix1[i][0] )
        align2.insert(0,matrix1[0][j] )

        next="a"
        i=i-1
        j=j-1
        if trace==0:trace=" 0"
        matrix5[i][j]=trace
        trace=traceb(matrix1,i,j,matrix1[i][j]) 
        
    elif trace== matrix1[i][j-1]: #c
        align2.insert(0,matrix1[0][j] )
        align1.insert(0,"-")
        next="c"
        i=i
        j=j-1
        if trace==0:trace=" 0"
        matrix5[i][j]=trace
        trace=traceb(matrix1,i,j,matrix1[i][j])
        
    elif trace== matrix1[i-1][j]: #b
        align2.insert(0,"-" )
        align1.insert(0,matrix1[i][0])
        next="b"
        i=i-1
        j=j
        if trace==0:trace=" 0"
        matrix5[i][j]=trace
        trace=traceb(matrix1,i,j,matrix1[i][j])
        #print(trace) 
    

for i in range(1,len2+1): #columns
    
    for j in range(1,len1+1):#rows
        if matrix5[i][j]==0:
           matrix5[i][j]=""   
        matrix5[1][1]=0   
          
print("Alignment Matrix")
print
print (tabulate(matrix5,tablefmt="fancy_grid"))
print()

print("Alignment ")
print(*align2)   
print(*align1)

        
#print (tabulate(matrix1,tablefmt="fancy_grid"))
