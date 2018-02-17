import re
import sys
import numpy as np
#getting the input from the user
inputseq=[]
outputseq=[]

inputseq=sys.argv[1]
#initializing the variables
a=[0.7,0.3]
b1=[0.3,0.5]
b2=[0.35,0.1]
b3=[0.35,0.4]
rr=0.6
rs=0.4
sr=0.3
ss=0.7
R=[]
S=[]
i=0;
Rx=[]
Sx=[]

# This is the main logic of the program
for i in range(len(inputseq)):
    #it checks if the current input sequence is the first, in that case the implementation is different
    if(i==0):
        if(inputseq[i]=='W'):
            R.append(a[0]*b1[0])
            S.append(a[1]*b1[1])
            m=a[0]*b1[0]
            n=a[1]*b1[1]
            Rx.append("q0")
            Sx.append("q0")
        else:
            if(inputseq[i]=='C'):
                R.append(a[0] * b2[0])
                S.append(a[1] * b2[1])
                m = a[0] * b1[0]
                n = a[1] * b1[1]
                Rx.append("q0")
                Sx.append("q0")
            else:
                if(inputseq[i]=='S'):
                    R.append(a[0] * b3[0])
                    S.append(a[1] * b3[1])
                    m = a[0] * b1[0]
                    n = a[1] * b1[1]
                    Rx.append("q0")
                    Sx.append("q0")

    #This is the logic for all the other inputs
    else:
        if(inputseq[i]=='W'):
            m = R[i - 1] * rr * b1[0]
            n = S[i - 1] * sr * b1[0]
            temp1 = max(m, n)
            if (m > n):
                Rx.append("R")
            else:
                Rx.append("S")
            R.append(temp1)
            c = R[i - 1] * rs * b1[1]
            d = (S[i - 1] * ss * b1[1])
            temp2 = max(c, d)
            S.append(temp2)
            if (c > d):
                Sx.append("R")
            else:
                Sx.append("S")
        if(inputseq[i]=='C'):
            m = R[i - 1] * rr * b2[0]
            n = S[i - 1] * sr * b2[0]
            temp1 = max(m, n)
            if (m>n):
                Rx.append("R")
            else:
                Rx.append("S")
            R.append(temp1)
            c = R[i - 1] * rs * b2[1]
            d = (S[i - 1] * ss * b2[1])
            temp2 = max(c, d)
            S.append(temp2)
            if (c>d):
                Sx.append("R")
            else:
                Sx.append("S")


        if(inputseq[i]=='S'):
            m = R[i - 1] * rr * b3[0]
            n = S[i - 1] * sr * b3[0]
            temp1 = max(m, n)
            if (m > n):
                Rx.append("R")
            else:
                Rx.append("S")
            R.append(temp1)
            c = R[i - 1] * rs * b3[1]
            d = (S[i - 1] * ss * b3[1])
            temp2 = max(c, d)
            S.append(temp2)
            if (c > d):
                Sx.append("R")
            else:
                Sx.append("S")


# new.append(R)
# new.append(S)
# print(new[0])
# print(new[1])



# #this logic is for printing the final output
# str1=''.join(outputseq)
# print("The output for the given input sequence is :"+str1)

current=""
i=len(inputseq)-1
while(i>-1):
    if(i==len(inputseq)-1):
        if(R[i]>S[i]):
            outputseq.append("R")
            current="Rx"
            i-=1
            continue
        else:
            outputseq.append("S")
            current="Sx"
            i -= 1
            continue
    else:
        if(current=="Rx"):
            outputseq.append(Rx[i+1])
            if(Rx[i]=="R"):
                current="Rx"
                i -= 1
                continue
            else:
                current = "Sx"
                i -= 1
                continue
        else:
            outputseq.append(Sx[i+1])
            if (Sx[i] == "R"):
                current = "Rx"
                i -= 1
                continue
            else:
                current = "Sx"
                i -= 1
                continue
#currently printing reverse output
str1=''.join(reversed(outputseq))
print("The output sequence is: "+str1)
