'''Radix Sort takes in an unsorted list A and returns a sorted list B.
It uses Counting Sort for as a sub-routing in each step, so it is crucial
to understand Counting Sort to understand this algorithm.'''
def counting_sort_edited(A,index):
    A_with_zeroes = [f'{number:04d}' for number in A]
    correct_digit = [int(str(num)[index-1:index]) for num in A_with_zeroes]
    k = max(correct_digit)
    B = [0 for i in range(len(A))]
    C = [0 for j in range(k+1)]
    # incrementing indexation of digits
    for num in correct_digit:
        C[num] +=1
    # making C cumulative
    for i in range(len(C)):
        if i != 0:
            C[i] += C[i-1]
    # performing the sorting
    for i in range(len(A_with_zeroes),0,-1):
        B[C[correct_digit[int(i)-1]]-1] = A[int(i)-1]
        C[correct_digit[int(i)-1]] -= 1
    return B

def radix_sort(A):
    max_A = len(str(max(A)))
    for i in range(max_A,0,-1):
        A = counting_sort_edited(A,i)
        print(A)
    return A
unsorted = [4234,652,2343,435,69,23,231,1,45,23,474,2342,91,4563,123,6543,123,34,23,854,1,89,3,213,7654,9]
sorted = radix_sort(unsorted)