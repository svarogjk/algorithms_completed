from timeit import timeit

def insertion_sort(A: list)->list:
    '''
    :param A: unsorted array
    :return A: sorted array
    '''
    '''choose a key: current element from unsorted array'''
    for j in range(1, len(A)):
        key = A[j]
        '''insert it into sorted part'''
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


#merge procedure
def merge(A, p, q, r):
    '''divide the part of array on
    two parts: A[p..q] and A[q+1..r]. Then put A[p..q] into L-array (left array)
    and R-array (right array)'''
    #the length of A[p..q]
    #the new array
    A_1 = []
    n_1 = q - p
    #the length of A[q+1..r]
    n_2 = r - q
    L = []
    R = []
    #A[p..q] -> L[1..n_1]
    for i in range(n_1):
        L.append(A[p + i])
    #A[q+1..r] -> R[1..n_2]
    for j in range(n_2):
        R.append(A[q + j])
    #add the "limiters: inf" to both arrays
    L += [float("inf")]
    R += [float("inf")]
    '''go through the arrays, compare the pairs of elements
    and put the less one back to the new sorted array A_1'''
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A_1.append(L[i])
            i += 1
        else:
            A_1.append(R[j])
            j += 1
    return A_1


#merge_sort procedure
def merge_sort(A, p, r):
    A_out = []
    if (r - p == 1):
        return A[p:r]
    elif p < r:
        q = (p + r) // 2
        A_L = A[p:q]
        A_R = A[q:r]
        if len(A_L) > 4 or len(A_R) > 4:
            A_L = merge_sort(A_L, 0, len(A_L))
            A_R = merge_sort(A_R, 0, len(A_R))
        else:
            A_L = insertion_sort(A_L)
            A_R = insertion_sort(A_R)
            '''the execution time is two times more due to merge_sort only used
            accessed with timeit'''
            # A_L = merge_sort(A_L, 0, len(A_L))
            # A_R = merge_sort(A_R, 0, len(A_R))

        A_out = merge(A_L + A_R, p, q, r)
    return A_out


if __name__ == '__main__':
    from unittest import TestCase, main

    A = [9, 3, 6, 5, 4, 1, 2, 17, 15, 5]
    print(f'A before sorting procedure = {A}')
    q = len(A) // 2
    # A_1 = merge(A=A, q=q, p=0, r=len(A))
    A_1 = merge_sort(A=A, p=0, r=len(A))
    # A_1 = insertion_sort(A)
    print(f'A after sorting procedure = {A_1}')

    print(timeit('merge_sort(A=A, p=0, r=len(A))', 'from __main__ import merge_sort, A',
                 number=100000))



    class SimpleTest(TestCase):

        def test(self):
            self.assertEqual(A_1, sorted(A))

    main()














