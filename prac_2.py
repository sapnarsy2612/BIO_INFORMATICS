se1=input("Enter the first sequence::")
se2=input("Enter the second sequence::")
seq1=list(se1)
seq2=list(se2)
score=[]
def find_identity(a,b):
     gap(a,b)
     print(a)
     print(b)
     score=0
     length=len(a)
     total_element=len(a)*len(b)
     for i in range(0,length):
          for j in range(0,length):
               if(a[i]==b[i]):
                    score+=1
     identity=(score/total_element)*100
     print("Matching score::",score)
     print("Identity of the sequences::",identity)
def gap(a,b):
     if(len(a)==len(b)):
          print()
     else:
          k=int(input("Enter the position to insert gap::"))
          if(len(a)<len(b)):
               a.insert(k,'-')
          else:
               b.insert(k,'-')
find_identity(seq1,seq2)
