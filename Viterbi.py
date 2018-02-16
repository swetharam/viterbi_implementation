import re
import sys
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

# This is the main logic of the program
for i in range(len(inputseq)):
    #it checks if the current input sequence is the first, in that case the implementation is different
    if(i==0):
        if(inputseq[i]=='W'):
            R.append(a[0]*b1[0])
            S.append(a[1]*b1[1])
            if(R[i]> S[i]):
                outputseq.append("R")
            else:
                outputseq.append("S")
        else:
            if(inputseq[i]=='C'):
                R.append(a[0] * b2[0])
                S.append(a[1] * b2[1])
                if (R[i] > S[i]):
                    outputseq.append("R")
                else:
                    outputseq.append("S")
            else:
                if(inputseq[i]=='S'):
                    R.append(a[0] * b3[0])
                    S.append(a[1] * b3[1])
                    if (R[i] > S[i]):
                        outputseq.append("R")
                    else:
                        outputseq.append("S")

    #This is the logic for all the other inputs
    else:
        if(inputseq[i]=='W'):
            temp1=max(R[i-1]*rr,S[i-1]*sr)
            R.append(b1[0]*temp1)
            temp2=max((R[i-1]*rs),(S[i-1]*ss))
            S.append(b1[1]*temp2)
            if (R[i] > S[i]):
                outputseq.append("R")
            else:
                outputseq.append("S")

        if(inputseq[i]=='C'):
            temp1 = max(R[i - 1] * rr, S[i - 1] * sr)
            R.append(b2[0] * temp1)
            temp2 = max((R[i - 1] * rs), (S[i - 1] * ss))
            S.append(b2[1] * temp2)
            if (R[i] > S[i]):
                outputseq.append("R")
            else:
                outputseq.append("S")

        if(inputseq[i]=='S'):
            temp1 = max(R[i - 1] * rr, S[i - 1] * sr)
            R.append(b3[0] * temp1)
            temp2 = max(R[i - 1] * rs, S[i - 1] * ss)
            S.append(b3[1] * temp2)
            if (R[i] > S[i]):
                outputseq.append("R")
            else:
                outputseq.append("S")

str1=''.join(outputseq)
print(str1)


