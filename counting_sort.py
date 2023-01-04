''' takes in a list A and returns a sorted version of the same numbers.
does NOT use comparison, does its magic through directly accessing
indexes. Condition is that the numbers contained are between 
0 and some k>0'''
def counting_sort(A):
    # the length for our working list shall be the highest number. 
    k = max(A)
    # create output list, fill with zeroes
    B = [0 for i in range(len(A))]
    # create amount of numbers on each index list, fill with zeroes
    C = [0 for j in range(k+1)]
    #iterates each element in A and increments that index in C.
    for num in A:
        C[num] +=1
        print(C)
    print(C)
    # making C cumulative, because this will help us place the numbers back into B
    for i in range(len(C)):
        if i != 0:
            C[i] += C[i-1]
    print(C)
    # now we will put the numbers back into B, taking use of both A and C
    # iterating through A backwords and decrementing the position in C such
    # that we place the number one step before another number if the number is
    # the same
    for i in range(len(A),0,-1):
        B[C[A[i-1]]-1] = A[i-1]
        C[A[i-1]] -= 1
    return B

sorted = counting_sort([5,3,2,6,8,3,3,2,1,0,3,8])
print(sorted)