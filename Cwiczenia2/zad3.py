def find_sum(A):
   if len(A) < 4:
       return False
   for pocz in range(0,len(A)):
       for kon in range(pocz+1,len(A)):
           x = A[pocz] + A[kon]
           i = pocz + 1
           j = kon - 1
           while i < j:
               if x == A[i] + A[j]:
                   return True
               if x > A[i] + A[j]:
                   i += 1
               else:
                   j -= 1
   return False